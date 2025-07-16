from fastapi.routing import APIRouter

from typing import Any
from pydantic import EmailStr


router = APIRouter(
    prefix= "/orders",
    tags=["orders"]
)

@router.get("/")
def get_orders(
    skip: int = 0, limit: int = 25
) -> Any:
    """
    Get All orders
    """

    return

@router.get("/myOrders")
def get_my_orders(
    email: EmailStr
) -> Any:
    """
    Get my orders
    """

    return


@router.post("/newOrder")
def create_new_order(

) -> Any:
    """
    Create a new Order
    """

    return