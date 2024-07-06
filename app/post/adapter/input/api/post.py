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
):
    return []

