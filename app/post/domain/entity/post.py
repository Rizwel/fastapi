from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from core.db import Base
from core.db.mixins import TimestampMixin


class Post(Base, TimestampMixin):
    __tablename__ = "post"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    content: Mapped[str] = mapped_column(String(255), nullable=False)
    title: Mapped[str] = mapped_column(String(255), nullable=False)


class PostRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int = Field(..., title="POST ID")
    content: str = Field(..., title="Content")
    title: str = Field(..., title="Title")
