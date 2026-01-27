from llms.factory import get_openai_model_direct
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda


# Task 1: First Prompt (Question Answering)
prompt_template = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("user", "{input}")
])

# Task 2: LLM
llm_openai = get_openai_model_direct()

# Task 3: Output Parser
str_parser = StrOutputParser()


# Task 4: Custom Runnable (convert text to dictionary)
def dictionary_maker(text: str) -> dict:
    return {"text": text}

dictionary_maker_runnable = RunnableLambda(dictionary_maker)


# Task 5: Second Prompt (Post Generator)
prompt_post = ChatPromptTemplate.from_messages([
    ("system", "You're a social post generator."),
    ("user", "Create a post for the following text for LinkedIn: {text}")
])


# Create full chain:
# Prompt → LLM → String → Dict → Post Prompt → LLM → String
chain = (
    prompt_template
    | llm_openai
    | str_parser
    | dictionary_maker_runnable
    | prompt_post
    | llm_openai
    | str_parser
)

# Invoke the chain
response = chain.invoke({"input": "What is the capital of France?"})

# Print final result
print(response)
