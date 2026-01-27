# llms/openai.py

from langchain_openai import ChatOpenAI
from langchain.chat_models import init_chat_model
from core import settings


# -------- Option 1: Direct OpenAI way (Simple & Recommended for now) --------

def get_openai_model_direct():
    """
    Returns an OpenAI chat model using ChatOpenAI (direct provider binding).
    Best for learning and simple projects.
    """
    return ChatOpenAI(
        model="gpt-5-mini",
        temperature=0,
        api_key=settings["OPENAI_API_KEY"]
    )


# -------- Option 2: Unified loader way (Advanced & Multi-LLM ready) --------

def get_openai_model_unified():
    """
    Returns an OpenAI chat model using init_chat_model (provider-agnostic).
    Best for future multi-provider and production systems.
    """
    return init_chat_model(
        model="gpt-5-mini",
        temperature=0,
        api_key=settings["OPENAI_API_KEY"]
    )
