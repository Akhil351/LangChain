from llms.factory import get_openai_model_direct
from models.schemas import MovieReviewSchema
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda, RunnableBranch


# ---------------- Task 1: Movie Review Classification Prompt ----------------

prompt_template = ChatPromptTemplate.from_messages([
    ("system", "You are a movie review evaluator."),
    ("user", "Please categorize the following movie review as positive or negative:\n{input}")
])

# ---------------- Task 2: LLM ----------------

llm_openai = get_openai_model_direct()

# Structured output (Pydantic)
llm_structured = llm_openai.with_structured_output(MovieReviewSchema)


# ---------------- Task 3: Extract sentiment as string ----------------

def extract_sentiment(result: MovieReviewSchema) -> str:
    return result.model_dump()["movie_summary_flag"]

extract_sentiment_runnable = RunnableLambda(extract_sentiment)


# ---------------- Conditional Branch 1: LinkedIn Generator ----------------

str_parser = StrOutputParser()

linkedin_prompt = ChatPromptTemplate.from_messages([
    ("system", "You're a LinkedIn post generator."),
    ("user", "Create a post for the following text for LinkedIn: {text}")
])

chain_linkedin = linkedin_prompt | llm_openai | str_parser


# ---------------- Conditional Branch 2: Instagram Generator ----------------

def insta_chain(text: dict):
    insta_prompt = ChatPromptTemplate.from_messages([
        ("system", "You're an Instagram post generator."),
        ("user", "Create a post for the following text for Instagram: {text}")
    ])

    chain_insta = insta_prompt | llm_openai | str_parser
    return chain_insta.invoke(text)

insta_chain_runnable = RunnableLambda(insta_chain)


# ---------------- Conditional Routing ----------------

conditional_chain = RunnableBranch(
    (lambda sentiment: sentiment == "positive", chain_linkedin),
    insta_chain_runnable  # default (negative)
)


# ---------------- Final Chain ----------------

final_chain = (
    prompt_template
    | llm_structured
    | extract_sentiment_runnable
    | conditional_chain
)

# ---------------- Invoke ----------------

response = final_chain.invoke({
    "input": "The movie was fantastic with stunning visuals and a gripping storyline."
})

print(response)
