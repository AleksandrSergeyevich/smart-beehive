from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime

router = APIRouter()


class SensorReading(BaseModel):
    beehive_id: int
    timestamp: datetime
    temperature: float
    humidity: float
    weight: float


@router.get("/{beehive_id}/latest", response_model=SensorReading)
def get_latest_reading(beehive_id: int):
    return SensorReading(
        beehive_id=beehive_id,
        timestamp=datetime.utcnow(),
        temperature=34.5,
        humidity=62.0,
        weight=42.3,
    )
