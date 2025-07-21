from fastapi.routing import APIRouter
from app.api.v1 import category, order, product

router = APIRouter()

router.include_router(product.router)
router.include_router(category.router)
router.include_router(order.router)

__all__ = ["router"]