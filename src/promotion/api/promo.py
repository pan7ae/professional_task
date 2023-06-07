from typing import List, Optional

from fastapi import APIRouter, Depends, status

from .depends import get_promo_service
from ..models.prize import PrizeCreate
from ..models.promotion import Promo, PromoWithDetails, PromoCreate, PromoUpdate
from ..models.result import Result
from ..models.user import UserCreate
from ..services.promo import PromoService

router = APIRouter(
    prefix='/promo'
)


@router.get("/", response_model=List[Promo])
async def get_promotions(service: PromoService = Depends(get_promo_service)):
    return await service.get_list()


@router.post("/", response_model=Optional[int], status_code=status.HTTP_201_CREATED)
async def create_promotion(
    promo_data: PromoCreate = Depends(PromoCreate.as_form),
    service: PromoService = Depends(get_promo_service)):
    return await service.create(promo_data)


@router.get("/{promo_id}", response_model=PromoWithDetails)
async def get_promotion(
    promo_id: int,
    service: PromoService = Depends(get_promo_service)):
    return await service.get(promo_id)


@router.put("/{promo_id}", response_model=Promo)
async def update_promotion(
    promo_id: int,
    promo_data: PromoUpdate = Depends(PromoUpdate.as_form),
    service: PromoService = Depends(get_promo_service)):
    return await service.update(promo_id, promo_data)


@router.delete("/{promo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_promotion(
    promo_id: int,
    service: PromoService = Depends(get_promo_service)):
    return await service.delete(promo_id)
