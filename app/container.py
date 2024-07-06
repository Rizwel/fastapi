from dependency_injector.containers import DeclarativeContainer, WiringConfiguration
from dependency_injector.providers import Factory, Singleton

from app.auth.application.service.jwt import JwtService
from app.user.adapter.output.persistence.repository_adapter import UserRepositoryAdapter
from app.user.adapter.output.persistence.sqlalchemy.user import UserSQLAlchemyRepo
from app.user.application.service.user import UserService

from app.post.adapter.output.persistence.repository_adapter import PostRepositoryAdapter
from app.post.adapter.output.persistence.sqlalchemy.post import PostSQLAlchemyRepo
from app.post.application.service.user import PostService


class Container(DeclarativeContainer):
    wiring_config = WiringConfiguration(packages=["app"])

    user_repo = Singleton(UserSQLAlchemyRepo)
    user_repo_adapter = Factory(UserRepositoryAdapter, user_repo=user_repo)
    user_service = Factory(UserService, repository=user_repo_adapter)

    post_repo = Singleton(PostSQLAlchemyRepo)
    post_repo_adapter = Factory(PostRepositoryAdapter, repository=post_repo)
    post_service = Factory(PostService, repository=post_repo_adapter)

    jwt_service = Factory(JwtService)
