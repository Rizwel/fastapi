from abc import ABC, abstractmethod
from app.post.domain.entity.post import Post


class PostRepo(ABC):
    @abstractmethod
    async def get_posts(
            self,
            *,
            limit: int = 12,
            prev: int | None = None,
    ) -> list[Post]:
        """Get post list"""

    @abstractmethod
    async def get_post_by_id(self, *, post_id: int) -> Post | None:
        """Get post by id"""

    @abstractmethod
    async def save(self, *, post: Post) -> None:
        """Save post"""
