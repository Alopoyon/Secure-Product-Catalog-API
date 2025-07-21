from fastapi.routing import APIRouter
from fastapi.exceptions import HTTPException

from typing import Any

router = APIRouter(
    prefix="/categories",
    tags=["categories"]
)


@router.get("/")
def get_categories(
    skip: int = 0, limit: int = 25
) -> Any:
    """
    Get available categories
    """

    return

@router.post("/newCategory")
def create_new_category(
    name: str, description: str|None = None
) -> Any:
    """
    Create a new category
    """

    return