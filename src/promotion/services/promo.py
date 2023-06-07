from typing import List

from databases import Database
from fastapi import HTTPException, status

from ..db.promotion import promotions
from ..models.promotion import Promo, PromoWithDetails, PromoCreate, PromoUpdate


class PromoService:
    def __init__(self, database: Database):
        self.database = database

    async def get_promo_with_details(self, promo_id: int) -> PromoWithDetails:
        query = promotions.select().where(promotions.c.id == promo_id)
        promo = await self.database.fetch_one(query=query)

        if not promo:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return PromoWithDetails.parse_obj(promo)

    async def get_promo_list(self) -> List[Promo]:
        query = promotions.select()
        return await self.database.fetch_all(query=query)

    async def get_promo(self, promo_id: int) -> PromoWithDetails:
        return await self.get_promo_with_details(promo_id)

    async def create_promo(self, promo_data: PromoCreate):
        promo = PromoCreate(**promo_data.dict())

        values = {**promo.dict()}
        query = promotions.insert().values(**values)
        promo_res = await self.database.execute(query=query)
        return promo_res

    async def update_promo(self, promo_id: int, promo_data: PromoUpdate) -> Promo:
        promo = await self.get_promo_with_details(promo_id)

        for field, value in promo_data:
            if value:
                setattr(promo, field, value)

        values = {**promo.dict()}
        query = promotions.update().where(promotions.c.id == promo_id).values(**values)
        await self.database.execute(query=query)
        return promo

    async def delete_promo(self, promo_id: int) -> None:
        await self.get_promo_with_details(promo_id)

        query = promotions.delete().where(promotions.c.id == promo_id)
        return await self.database.execute(query=query)

