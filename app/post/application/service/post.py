from app.post.domain.usecase.post import PostUseCase
from app.post.adapter.output.persistence.repository_adapter import PostRepositoryAdapter


class PostService(PostUseCase):

    def __init__(self, *, repository: PostRepositoryAdapter):
        self.repository = repository

    async def get_post_list(
            self,
            *,
            limit: int = 12,
            prev: int | None = None,
    ) -> list[Post]:
        return await self.repository.get_posts(limit=limit, prev=prev)

    async def get_post_by_id(self, *, post_id: int) -> Post | None:
        return await self.repository.get_post_by_id(post_id=post_id)

    async def create_post(self, *, command: CreatePostCommand) -> None:
        post = Post.from_dict(command.dict())
        await self.repository.save(post=post)
        return None



