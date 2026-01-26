from llms.factor import get_openai_model_direct
from langchain_core.messages import SystemMessage, HumanMessage

# Get OpenAI chat model from factory
llm_openai = get_openai_model_direct()

# Define conversation messages
messages = [
    SystemMessage(content="You are a Gen Z assistant who always replies in a fun and casual style."),
    HumanMessage(content="Bro, tell me a fun fact")
]

# Invoke the model with structured messages
response = llm_openai.invoke(messages)

# Print the assistant's reply
print(response.content)
