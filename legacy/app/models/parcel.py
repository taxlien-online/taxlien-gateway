from sqlalchemy import Column, String, JSON, DateTime, Integer, UniqueConstraint
from app.core.db import Base
from datetime import datetime

class Parcel(Base):
    __tablename__ = "parcels"

    id = Column(Integer, primary_key=True, autoincrement=True)
    parcel_id = Column(String, nullable=False, index=True)
    platform = Column(String, nullable=False, index=True)
    state = Column(String, nullable=False, index=True)
    county = Column(String, nullable=False, index=True)
    data = Column(JSON, nullable=False)
    scraped_at = Column(DateTime, default=datetime.utcnow)
    worker_id = Column(String, nullable=True)

    __table_args__ = (
        UniqueConstraint('parcel_id', 'platform', 'state', 'county', name='_parcel_platform_uc'),
    )
