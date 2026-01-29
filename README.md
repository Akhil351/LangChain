# LangChain Tutorial 🦜🔗

A comprehensive hands-on tutorial project for learning LangChain fundamentals, covering everything from basic chat models to advanced ReAct agents with tool integration.

## 📚 Overview

This repository contains practical examples and implementations demonstrating core LangChain concepts, organized into progressive chapters. Each example is designed to be self-contained and easy to understand, making it perfect for both beginners and intermediate developers looking to master LangChain.

## ✨ Features

### Chapter 1: Foundation - Chat Models & Prompts
- **ChatOpenAI**: Direct integration with OpenAI's chat models
- **InitChatModel**: Model initialization patterns and best practices
- **Messages**: Working with different message types and formats
- **Prompts**: Template-based prompt engineering (Parts 1 & 2)
- **Structured Output**: Type-safe responses with Pydantic models

### Chapter 2: Chains & Composition
- **First Chain**: Building your first LangChain pipeline
- **Runnable**: Understanding the Runnable interface
- **Custom Runnable**: Creating custom chain components
- **Parallel Chains**: Executing multiple chains concurrently
- **Conditional Chains**: Dynamic routing and branching logic

### Chapter 3: Agents & Tools
- **ReAct Agent**: Reasoning + Acting pattern with tool integration
- **ReAct DB Agent**: Database-aware agents for data queries

## 🛠️ Tech Stack

- **Python**: 3.11+
- **LangChain**: Core framework for LLM applications
- **OpenAI**: GPT models integration
- **SQLAlchemy**: Database ORM
- **PostgreSQL**: Database backend (psycopg2-binary)
- **Wikipedia API**: Knowledge base integration
- **UV**: Fast Python package manager

## 📋 Prerequisites

Before you begin, ensure you have:

- Python 3.11 or higher installed
- An OpenAI API key ([Get one here](https://platform.openai.com/api-keys))
- UV package manager (recommended) or pip
- PostgreSQL (for database examples)

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/langchain-tutorial.git
cd langchain-tutorial
```

### 2. Install UV (if not already installed)

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 3. Install dependencies

```bash
uv sync
```

Or using pip:

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

Create a `.env` file in the root directory:

```bash
OPENAI_API_KEY=your_openai_api_key_here
```

## 📂 Project Structure

```
LangChain/
├── Chapter1/              # Foundation concepts
│   ├── 1_ChatOpenAI.py
│   ├── 2_InitChatModel.py
│   ├── 3_Messages.py
│   ├── 4_Prompts1.py
│   ├── 5_Prompts2.py
│   └── 6_Structured_Output.py
├── Chapter2/              # Chains and composition
│   ├── 1_FirstChain.py
│   ├── 2_Runnable.py
│   ├── 3_CustomRunnable.py
│   ├── 4_ParallelChains.py
│   └── 5_ConditonalChains.py
├── Chapter3/              # Agents and tools
│   ├── 1_ReActAgent.py
│   └── 2_ReAct_DBAgent.py
├── core/                  # Core configuration
│   ├── config.py          # Environment settings
│   └── deps.py            # Dependencies
├── database/              # Database utilities
│   └── db.py
├── llms/                  # LLM factory patterns
│   └── factory.py
├── models/                # Data models
│   └── schemas.py
├── main.py                # Entry point
├── pyproject.toml         # Project dependencies
└── README.md
```

## 💻 Usage

### Running Individual Examples

Navigate to any chapter and run the examples:

```bash
# Chapter 1 - Basic chat interaction
python Chapter1/1_ChatOpenAI.py

# Chapter 2 - Chain composition
python Chapter2/1_FirstChain.py

# Chapter 3 - ReAct agent with tools
python Chapter3/1_ReActAgent.py
```

### Using the LLM Factory

The project includes a factory pattern for model initialization:

```python
from llms.factory import get_openai_model_direct

# Initialize the model
llm = get_openai_model_direct()

# Use the model
response = llm.invoke("Your prompt here")
print(response.content)
```

## 🎯 Key Concepts Covered

### 1. **Chat Models**
Learn how to initialize and interact with OpenAI's chat models, handle different message types, and work with model responses.

### 2. **Prompt Engineering**
Master template-based prompts, variable substitution, and structured prompt design for consistent outputs.

### 3. **Chains (LCEL)**
Build complex workflows using LangChain Expression Language (LCEL), compose chains, and handle parallel execution.

### 4. **Agents & Tools**
Implement ReAct (Reasoning + Acting) agents that can use external tools like web search, Wikipedia, and custom enterprise functions.

### 5. **Structured Outputs**
Work with type-safe responses using Pydantic models for reliable data extraction.

## 🔧 Configuration

The project uses environment-based configuration managed through `core/config.py`:

```python
from core.config import settings

# Access configuration
api_key = settings["OPENAI_API_KEY"]
```

## 📦 Dependencies

Key packages used in this project:

- `langchain` - Core LangChain framework
- `langchain-openai` - OpenAI integration
- `langchain-community` - Community tools (Wikipedia, DuckDuckGo)
- `openai` - Official OpenAI client
- `sqlalchemy` - Database ORM
- `psycopg2-binary` - PostgreSQL adapter
- `python-dotenv` - Environment variable management
- `wikipedia` - Wikipedia API wrapper

## 📖 Learning Path

Recommended order for beginners:

1. **Start with Chapter 1** - Get comfortable with chat models and prompts
2. **Progress to Chapter 2** - Learn about chains and composition
3. **Advance to Chapter 3** - Master agents and tool integration
4. **Explore the core modules** - Understand the project architecture

## 🤝 Contributing

Contributions are welcome! Feel free to:

- Report bugs
- Suggest new examples
- Improve documentation
- Add more chapters

## 📝 License

This project is open source and available under the MIT License.

## 🔗 Resources

- [LangChain Documentation](https://python.langchain.com/)
- [OpenAI API Reference](https://platform.openai.com/docs)
- [LangChain Expression Language (LCEL)](https://python.langchain.com/docs/expression_language/)
- [ReAct Paper](https://arxiv.org/abs/2210.03629)

## 💡 Tips

- Always set your `OPENAI_API_KEY` before running examples
- Start with smaller models for testing (e.g., `gpt-3.5-turbo`)
- Review the comments in each file for detailed explanations
- Experiment with different prompts and parameters

## 🙋‍♂️ Support

If you have questions or run into issues:

1. Check the code comments for inline documentation
2. Review the LangChain official docs
3. Open an issue in this repository

---

**Happy Learning! 🚀**

Built with ❤️ using LangChain and OpenAI
