from pydantic import BaseModel


class CreatePostCommand(BaseModel):
    title: str
    content: str
