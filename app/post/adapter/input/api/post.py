from dependency_injector.wiring import inject
from fastapi import APIRouter, Query

from app.post.adapter.input.api.response import PostListResponse

post_router = APIRouter()


@post_router.get(
    "",
    response_model=list[PostListResponse],
    dependencies=[],
)
@inject
async def get_post_list(
    limit: int = Query(10, description="Limit"),
    prev: int = Query(None, description="Prev ID"),
    usecase: PostUseCase = Depends(Provide[Container.post_service]),
):
    return await usecase.get_post_list(limit=limit, prev=prev)


@post_router.get(
    "/{post_id}",
    response_model=PostListResponse,
    dependencies=[],
)
@inject
async def get_post_by_id(
    post_id: int,
    usecase: PostUseCase = Depends(Provide[Container.post_service]),
):
    return await usecase.get_post_by_id(post_id=post_id)

@post_router.post(
    "",
    response_model=PostListResponse,
)
@inject
async def create_post(
    request: CreatePostRequest,
    usecase: PostUseCase = Depends(Provide[Container.post_service]),
):
    command = CreatePostCommand(**request.model_dump())
    await usecase.create_post(command=command)
    return {"title": request.title, "content": request.content}
