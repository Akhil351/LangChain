from llms.factory import get_openai_model_direct
from langchain_core.prompts import PromptTemplate

# Get OpenAI chat model from factory
llm_openai = get_openai_model_direct()

# Take user input
user_input = input("Enter your message: ")

# Create prompt template
prompt = PromptTemplate.from_template("{user_input}")

# Format prompt with user input
formatted_prompt = prompt.invoke({"user_input": user_input})

# Invoke model using the formatted prompt (as plain text)
response = llm_openai.invoke(formatted_prompt.to_string())

# Print assistant reply
print(response.content)
