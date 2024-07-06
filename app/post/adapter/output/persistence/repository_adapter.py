from app.post.domain.entity.post import Post, PostRead
from app.post.domain.repository.post import PostRepo


class PostRepositoryAdapter:
    def __init__(self, *, user_repo: UserRepo):
        self.user_repo = user_repo

    async def get_posts(
            self,
            *,
            limit: int = 12,
            prev: int | None = None,
    ) -> list[PostRead]:
        posts = await self.post_repo.get_posts(limit=limit, prev=prev)
        return [PostRead.model_validate(post) for post in posts]

    async def get_post_by_id(self, *, post_id: int) -> Post | None:
        return await self.post_repo.get_post_by_id(post_id=post_id)

    async def save(self, *, post: Post) -> None:
        await self.post_repo.save(post=post)
