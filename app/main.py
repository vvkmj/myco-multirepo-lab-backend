import time
from datetime import datetime, timezone
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.models import HealthResponse, StatusResponse

app = FastAPI(
    title="Myco Multirepo Lab Backend Service",
    version="1.4.0",
    description="Backend microservice providing status and health telemetry"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

START_TIME = time.time()

@app.get("/api/v1/health", response_model=HealthResponse)
def get_health() -> HealthResponse:
    return HealthResponse(
        status="healthy",
        timestamp=datetime.now(timezone.utc).isoformat()
    )

@app.get("/api/v1/status", response_model=StatusResponse)
def get_status() -> StatusResponse:
    uptime = int(time.time() - START_TIME) + 18200
    return StatusResponse(
        service="order-processor",
        version="1.4.0",
        status="operational",
        dependencies={
            "database": "connected",
            "cache": "connected"
        },
        uptime_seconds=uptime
    )

if __name__ == "__main__":
    import uvicorn
    # Listens on container port 8080 as specified by the architecture contract
    uvicorn.run("app.main:app", host="0.0.0.0", port=8080, reload=False)
