from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api.beehives import router as beehives_router
from src.api.sensors import router as sensors_router

app = FastAPI(title="Smart Beehive API", version="0.2.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(beehives_router, prefix="/api/v1/beehives", tags=["beehives"])
app.include_router(sensors_router, prefix="/api/v1/sensors", tags=["sensors"])


@app.get("/health")
def health_check():
    return {"status": "ok", "version": "0.2.0"}
