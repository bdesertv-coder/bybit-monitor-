from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.services.bybit_client import BybitClient
from app.database import get_db
from app.models.price import Price

router = APIRouter()
client = BybitClient()

@router.get("/price/{symbol}")
async def get_price(symbol: str, db: AsyncSession = Depends(get_db)):
    data = client.get_ticker(symbol)
    if data is None:
        raise HTTPException(status_code=404, detail="Пара не найдена")

    # Сохраняем в БД
    record = Price(
        symbol=data["symbol"],
        price=data["price"],
        volume_24h=data["volume_24h"]
    )
    db.add(record)
    await db.commit()

    return data

@router.get("/orderbook/{symbol}")
def get_orderbook(symbol: str):
    data = client.get_orderbook(symbol)
    if data is None:
        raise HTTPException(status_code=404, detail="Пара не найдена")
    return data

# Новый эндпоинт — история цен из БД
@router.get("/history/{symbol}")
async def get_history(symbol: str, db: AsyncSession = Depends(get_db)):
    result = await db.execute(
        select(Price)
        .where(Price.symbol == symbol.upper())
        .order_by(Price.timestamp.desc())
        .limit(50)  # последние 50 записей
    )
    records = result.scalars().all()
    return records