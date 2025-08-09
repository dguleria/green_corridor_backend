
from fastapi import APIRouter
from typing import List

router = APIRouter()

# Mock vulnerability data to simulate RiskSense API
mock_vulnerabilities = [
    {"id": 1, "asset": "app-server-1", "risk_score": 85, "status": "open", "description": "SQL Injection vulnerability"},
    {"id": 2, "asset": "db-server-2", "risk_score": 70, "status": "open", "description": "Outdated software version"},
    {"id": 3, "asset": "api-gateway", "risk_score": 95, "status": "closed", "description": "Authentication bypass attempt"},
]

@router.get("/risksense/vulnerabilities", response_model=List[dict])
async def get_vulnerabilities():
    return mock_vulnerabilities
