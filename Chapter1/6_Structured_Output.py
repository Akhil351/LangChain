from llms.factor import get_openai_model_direct
from langchain_core.prompts import PromptTemplate
from model import llm_schema1

# Get OpenAI chat model from factory
llm_openai = get_openai_model_direct()

# Take user input
user_input = input("Enter your message: ")

# Create prompt template
prompt = PromptTemplate.from_template("{user_input}")

# Format prompt with user input
formatted_prompt = prompt.invoke({"user_input": user_input})

# Enable structured output using schema
llm_structured_output = llm_openai.with_structured_output(llm_schema1)

# Invoke model using the formatted prompt
response = llm_structured_output.invoke(formatted_prompt.to_string())

# Print structured response and its type
print(response)
print(type(response))
