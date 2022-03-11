from ..services.promo import PromoService
from ..db.database import database


def get_promo_service() -> PromoService:
    return PromoService(database)
