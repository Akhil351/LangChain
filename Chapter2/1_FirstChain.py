from llms.factory import get_openai_model_direct
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


# Task 1: Prompt
prompt_template = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("user", "{input}")
])


# Task 2: LLM
llm_openai = get_openai_model_direct()

# Task 3: Output Parser
str_parser = StrOutputParser()

# Create chain: Prompt → LLM → Output Parser
chain = prompt_template | llm_openai | str_parser

# Invoke the chain
final_result = chain.invoke({"input": "What is the capital of France?"})

# Print final result
print(final_result)
