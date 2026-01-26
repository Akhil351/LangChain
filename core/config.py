import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


def get_settings() -> dict:
    """Load and return application settings from environment variables."""
    return {
        "OPENAI_API_KEY": os.getenv("OPENAI_API_KEY", ""),
    }


# Create settings instance
settings = get_settings()

