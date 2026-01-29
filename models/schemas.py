from sqlalchemy import Column, Integer, String, Numeric
from database import Base
from pydantic import BaseModel, Field
from typing import TypedDict, Literal


# ---------------- LLM / API Schemas ----------------

class JokeSchema(BaseModel):
    setup: str = Field(description="Introduces the joke")
    punchline: str = Field(description="Delivers the punchline")


class JokeSchemaDict(TypedDict):
    setup: str
    punchline: str


class MovieReviewSchema(BaseModel):
    sentiment: Literal["positive", "negative"]


# ---------------- Database Model ----------------

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    customer_name = Column(String, nullable=False)
    product_name = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)

    price = Column(Numeric(10, 2), nullable=False)
    total = Column(Numeric(10, 2), nullable=False)
