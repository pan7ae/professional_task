from typing import List, Optional

from fastapi import APIRouter, Depends, status

from .depends import get_promo_service
from ..models.models import PrizeCreate
from ..models.models import Promo, PromoWithDetails, PromoCreate, PromoUpdate
from ..models.models import Result
from ..models.models import UserCreate
from ..services.promo import PromoService

router = APIRouter(
    prefix='/promo'
)


@router.get("/", response_model=List[Promo])
async def get_promotions(service: PromoService = Depends(get_promo_service)) -> List[Promo]:
    return await service.get_promo_list()


@router.post("/", response_model=Optional[int], status_code=status.HTTP_201_CREATED)
async def create_promotion(
    promo_data: PromoCreate = Depends(PromoCreate.as_form),
    service: PromoService = Depends(get_promo_service)) -> Optional[int]:
    return await service.create_promo(promo_data)


@router.get("/{promo_id}", response_model=PromoWithDetails)
async def get_promotion(
    promo_id: int,
    service: PromoService = Depends(get_promo_service)) ->PromoWithDetails:
    return await service.get_promo(promo_id)


@router.put("/{promo_id}", response_model=Promo)
async def update_promotion(
    promo_id: int,
    promo_data: PromoUpdate = Depends(PromoUpdate.as_form),
    service: PromoService = Depends(get_promo_service)) -> Promo:
    return await service.update_promo(promo_id, promo_data)


@router.delete("/{promo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_promotion(
    promo_id: int,
    service: PromoService = Depends(get_promo_service)) -> None:
    return await service.delete_promo(promo_id)
