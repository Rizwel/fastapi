from dependency_injector.containers import DeclarativeContainer, WiringConfiguration
from dependency_injector.providers import Factory, Singleton

from app.post.adapter.output.persistence.repository_adapter import PostRepositoryAdapter
from app.post.adapter.output.persistence.sqlalchemy.post import PostSQLAlchemyRepo
from app.post.application.service.post import PostService


class PostContainer(DeclarativeContainer):
    wiring_config = WiringConfiguration(modules=["app"])

    post_sqlalchemy_repo = Singleton(PostSQLAlchemyRepo)
    post_repository_adapter = Factory(
        PostRepositoryAdapter,
        repository=post_sqlalchemy_repo,
    )
    post_service = Factory(PostService, repository=post_repository_adapter)
