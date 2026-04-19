from sqlalchemy import Column, Integer, String, Numeric, DateTime
from datetime import datetime
from app.database import Base

class Price(Base):
    __tablename__ = "prices"

    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String(20), nullable=False)
    price = Column(Numeric(20, 8), nullable=False)
    volume_24h = Column(Numeric(20, 2), nullable=True)
    timestamp = Column(DateTime, default=datetime.utcnow)