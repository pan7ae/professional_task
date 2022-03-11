from fastapi import APIRouter

from .promo import router as promo_router

router = APIRouter()
router.include_router(promo_router)
