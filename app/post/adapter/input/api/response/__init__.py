from pydantic import BaseModel, Field


class PostListResponse(BaseModel):
    title: str = Field(..., description="Title")
    content: str = Field(..., description="Content")
