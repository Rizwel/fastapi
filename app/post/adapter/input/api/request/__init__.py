from pydantic import BaseModel, Field


class CreatePostRequest(BaseModel):
    title: str = Field(..., description="Title")
    content: str = Field(..., description="Content")

