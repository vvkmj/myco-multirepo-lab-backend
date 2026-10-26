from typing import Dict
from pydantic import BaseModel, Field

class HealthResponse(BaseModel):
    status: str = Field(..., description="Overall health state")
    timestamp: str = Field(..., description="ISO formatted timestamp")

class StatusResponse(BaseModel):
    service: str = Field(..., description="Identifier name of the service")
    version: str = Field(..., description="Semantic version of the service")
    status: str = Field(..., description="Operational status: operational, degraded, or offline")
    dependencies: Dict[str, str] = Field(..., description="Status map of downstream dependencies")
    uptime_seconds: int = Field(..., description="Uptime duration in seconds")
