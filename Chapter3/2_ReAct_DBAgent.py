# ReAct: Reasoning + Acting (LLM + Tools)

from llms.factory import get_openai_model_direct
from langchain.tools import tool
from langchain.agents import create_agent
from decimal import Decimal

from core.deps import get_db
from models import Order


# ---------------- Initialize LLM ----------------

llm = get_openai_model_direct()


# ---------------- Tool 1: DB Tool (Fetch Purchase Details) ----------------

@tool
def get_customer_purchase_details(customer_name: str) -> str:
    """
    Use this tool to fetch purchased products with quantity, price, and total price
    for a given customer.
    """
    print("Tool Invoked: get_customer_purchase_details")
    with get_db() as db:
        orders = (
            db.query(
                Order.product_name,
                Order.quantity,
                Order.price,
                Order.total,
            )
            .filter(Order.customer_name.ilike(customer_name))
            .all()
        )

    if not orders:
        return f"No purchase records found for customer '{customer_name}'."

    response_lines = []
    grand_total = Decimal("0.00")

    for product, quantity, price, total in orders:
        response_lines.append(
            f"- {product}: Quantity={quantity}, Price={price}, Total={total}"
        )
        grand_total += total  # ✅ Decimal-safe addition

    return (
        f"Purchase details for '{customer_name}':\n"
        + "\n".join(response_lines)
        + f"\n\nGrand Total Amount: {grand_total}"
    )


# ---------------- Tool Kit ----------------

tools = [
    get_customer_purchase_details
]


# ---------------- ReAct Agent Initialization ----------------

agent = create_agent(
    llm,
    tools
)


# ---------------- ReAct Agent Invoke ----------------

result = agent.invoke(
    {
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are a ReAct agent that must decide when to use tools.\n\n"
                    "Tool usage rules:\n"
                    "1. ALWAYS use get_customer_purchase_details when the user asks about what a customer bought or purchased.\n"
                    "2. Always include quantity, price, and total price in the response.\n"
                )
            },
            {
                "role": "user",
                "content": (
                    "What did akhil buy?"
                )
            }
        ]
    }
)

final_message = result["messages"][-1]
print(final_message.content)
