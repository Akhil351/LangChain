from llms.factory import get_openai_model_direct
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda, RunnableParallel


# ---------------- Task 1: Movie Summarizer Prompt ----------------

prompt_template = ChatPromptTemplate.from_messages([
    ("system", "You are a movie summarizer."),
    ("user", "Please summarize the movie in brief: {input}")
])

# ---------------- Task 2: LLM (shared instance) ----------------

llm_openai = get_openai_model_direct()

# ---------------- Task 3: Output Parser ----------------

str_parser = StrOutputParser()


# ---------------- Task 4: Wrap summary into dictionary ----------------

def dictionary_maker(text: str) -> dict:
    return {"text": text}

dictionary_maker_runnable = RunnableLambda(dictionary_maker)


# ---------------- Parallel Branch 1: LinkedIn Post Generator ----------------

linkedin_prompt = ChatPromptTemplate.from_messages([
    ("system", "You're a LinkedIn post generator."),
    ("user", "Create a post for the following text for LinkedIn: {text}")
])

chain_linkedin = linkedin_prompt | llm_openai | str_parser


# ---------------- Parallel Branch 2: Instagram Post Generator ----------------

def insta_chain(text: dict):
    insta_prompt = ChatPromptTemplate.from_messages([
        ("system", "You're an Instagram post generator."),
        ("user", "Create a post for the following text for Instagram: {text}")
    ])

    chain_insta = insta_prompt | llm_openai | str_parser
    return chain_insta.invoke(text)

insta_chain_runnable = RunnableLambda(insta_chain)


# ---------------- Parallel Fan-Out Workflow ----------------

final_chain = (
    prompt_template
    | llm_openai
    | str_parser
    | dictionary_maker_runnable
    | RunnableParallel(
        branches={
            "linkedin": chain_linkedin,
            "instagram": insta_chain_runnable
        }
    )
)


# ---------------- Fan-In Step: Beautify Output ----------------

def final_output(final_response: dict) -> dict:
    linkedin_response = final_response["branches"]["linkedin"]
    instagram_response = final_response["branches"]["instagram"]

    return {
        "linkedin": linkedin_response,
        "instagram": instagram_response
    }

final_output_runnable = RunnableLambda(final_output)


# ---------------- Final Beautified Chain ----------------

beautified_chain = final_chain | final_output_runnable


# ---------------- Invoke the Workflow ----------------

response = beautified_chain.invoke({"input": "Avengers EndGame"})

# Print clean output
print("\n================ LinkedIn Post ================\n")
print(response["linkedin"])

print("\n================ Instagram Post ================\n")
print(response["instagram"])
