from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from datetime import datetime

router = APIRouter()


class Alert(BaseModel):
    id: int
    beehive_id: int
    alert_type: str
    message: str
    severity: str
    created_at: datetime


MOCK_ALERTS: list[Alert] = [
    Alert(
        id=1,
        beehive_id=1,
        alert_type="swarming",
        message="High probability of swarming detected",
        severity="warning",
        created_at=datetime(2026, 4, 1, 8, 30, 0),
    ),
    Alert(
        id=2,
        beehive_id=2,
        alert_type="temperature",
        message="Temperature above threshold: 41.2°C",
        severity="critical",
        created_at=datetime(2026, 4, 1, 9, 15, 0),
    ),
]


@router.get("/", response_model=list[Alert])
async def list_alerts(beehive_id: int | None = None) -> list[Alert]:
    if beehive_id is not None:
        return [a for a in MOCK_ALERTS if a.beehive_id == beehive_id]
    return MOCK_ALERTS


@router.get("/{alert_id}", response_model=Alert)
async def get_alert(alert_id: int) -> Alert:
    for alert in MOCK_ALERTS:
        if alert.id == alert_id:
            return alert
    raise HTTPException(status_code=404, detail="Alert not found")
