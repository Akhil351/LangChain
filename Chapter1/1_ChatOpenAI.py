from llms.factory import get_openai_model_direct

# Get OpenAI chat model from factory
llm_openai = get_openai_model_direct()

# Invoke the model with a prompt
response = llm_openai.invoke("Bro, tell me a fun fact")

# Print only the model response text
print(response.content)
