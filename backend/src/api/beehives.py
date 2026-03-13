from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()


class BeehiveStatus(BaseModel):
    id: int
    temperature: float
    humidity: float
    weight: float
    sound_level: float
    status: str


MOCK_DATA = {
    1: BeehiveStatus(id=1, temperature=34.5, humidity=62.0, weight=42.3, sound_level=0.4, status="normal"),
    2: BeehiveStatus(id=2, temperature=36.1, humidity=58.0, weight=38.7, sound_level=0.9, status="swarming"),
}


@router.get("/{beehive_id}/status", response_model=BeehiveStatus)
def get_beehive_status(beehive_id: int):
    if beehive_id not in MOCK_DATA:
        raise HTTPException(status_code=404, detail="Beehive not found")
    return MOCK_DATA[beehive_id]


@router.get("/", response_model=list[BeehiveStatus])
def list_beehives():
    return list(MOCK_DATA.values())
