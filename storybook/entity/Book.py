from pydantic import BaseModel, Field


class Book(BaseModel):
    title: str = Field(..., description="The title of the story")
    story: str = Field(..., description="The main text of the story")
    illustrations: list[str] = Field(..., description="List of illustrations")
