# ReAct: Reasoning + Acting (LLM + Tools)

from llms.factory import get_openai_model_direct
from langchain.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun, WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.agents import create_agent
import wikipedia


# ---------------- Initialize LLM ----------------

llm = get_openai_model_direct()


# ---------------- Tool 1: Web Search (DuckDuckGo) ----------------

duckduckgo_tool = DuckDuckGoSearchRun(
    description="Use this tool to search the web for current or real-time information."
)


# ---------------- Tool 2: Knowledge Lookup (Wikipedia) ----------------

wiki_wrapper = WikipediaAPIWrapper(
    wiki_client=wikipedia,
    top_k_results=3,
    lang="en"
)

wikipedia_tool = WikipediaQueryRun(
    api_wrapper=wiki_wrapper,
    description="Use this tool to look up factual and background information from Wikipedia."
)


# ---------------- Tool 3: Custom Enterprise Tool ----------------

@tool
def enterprise_tool(query: str) -> str:
    """
    Use this tool to send email notifications to your team.
    """
    print("Simulating sending email with content:")
    return "Email sent successfully."


# ---------------- Tool Kit ----------------

tools = [
    duckduckgo_tool,
    wikipedia_tool,
    enterprise_tool
]


# ---------------- ReAct Agent Initialization ----------------

agent = create_agent(
   llm
   ,tools
)

# ---------------- ReAct Agent Invoke  ----------------
result = agent.invoke(
    {"messages": [{"role": "user", "content": "AI is transforming the world. Can you provide me with the latest news about AI advancements? Also, send an email to notify my team about these advancements."}]}
)

final_message = result["messages"][-1]
print(final_message.content)