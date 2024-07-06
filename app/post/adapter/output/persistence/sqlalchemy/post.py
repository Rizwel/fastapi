from sqlalchemy import and_, or_, select

from app.post.domain.entity.post import Post
from app.post.domain.repository.post import PostRepo


class PostSQLAlchemyRepo(PostRepo):
    async def get_posts(
            self,
            *,
            limit: int = 12,
            prev: int | None = None,
    ) -> list[Post]:
        query = select(Post)

        if prev:
            query = query.where(Post.id < prev)

        if limit > 12:
            limit = 12

        query = query.limit(limit)
        async with session_factory() as read_session:
            result = await read_session.execute(query)

        return result.scalars().all()

    async def get_post_by_id(self, *, post_id: int) -> Post | None:
        async with session_factory() as read_session:
            stmt = await read_session.execute(select(Post).where(Post.id == post_id))
            return stmt.scalars().first()

    async def save(self, *, post: Post) -> None:
        session.add(post)
