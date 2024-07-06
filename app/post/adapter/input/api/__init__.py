from fastapi import APIRouter

from app.post.adapter.input.api.post import post_router

router = APIRouter()
router.include_router(post_router, prefix="/api/post", tags=["Post"])


__all__ = ["router"]
