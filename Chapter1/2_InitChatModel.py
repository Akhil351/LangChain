from llms.factory import get_openai_model_unified

# Get OpenAI chat model from unified factory
llm_openai = get_openai_model_unified()

# Invoke the model with a prompt
response = llm_openai.invoke("Bro, tell me a fun fact")

# Print only the model response text
print(response.content)
