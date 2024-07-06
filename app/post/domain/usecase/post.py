


class PostUseCase(ABC):
    @abstractmethod
    async def get_post_list(
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
    async def create_post(self, *, command: CreatePostCommand) -> None:
        """Create Post"""

