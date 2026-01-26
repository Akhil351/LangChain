from llms.factor import get_openai_model_direct
from langchain_core.prompts import ChatPromptTemplate

# Get OpenAI chat model from factory
llm_openai = get_openai_model_direct()

# Define chat prompt template
prompt_template = ChatPromptTemplate.from_messages([
    ("system", "You are a {tone} assistant."),
    ("user", "Write a fun fact about the {topic}.")
])

# Take user inputs
user_topic = input("Enter a topic: ")
user_tone = input("Enter a tone: ")

# Format the prompt with inputs
ready_prompt = prompt_template.invoke({
    "topic": user_topic,
    "tone": user_tone
})

# Invoke the model with formatted prompt
response = llm_openai.invoke(ready_prompt)

# Print only the assistant reply
print(response.content)
