from pydantic import BaseModel, Field
from typing import TypedDict

class llm_schema1(BaseModel):
    setup: str=Field(description="The setup of the joke")
    punchline: str=Field(description="The punchline of the joke")
    
class llm_schema2(TypedDict):
    setup: str
    punchline: str