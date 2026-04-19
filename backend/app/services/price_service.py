from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, desc
from decimal import Decimal
from typing import Optional, List
from app.models.price import Price


class PriceService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def save_price(
            self,
            symbol: str,
            price: Decimal,
            volume_24h: Optional[Decimal] = None
    ) -> Price:
        record = Price(
            symbol=symbol.upper(),
            price=price,
            volume_24h=volume_24h,
        )
        self.db.add(record)
        await self.db.commit()
        await self.db.refresh(record)
        return record

    async def get_last_prices(
            self,
            symbol: Optional[str] = None,
            limit: int = 10
    ) -> List[Price]:
        query = select(Price).order_by(desc(Price.timestamp))
        if symbol:
            query = query.where(Price.symbol == symbol.upper())
        query = query.limit(limit)

        result = await self.db.execute(query)
        return list(result.scalars().all())