
from fastapi import FastAPI, HTTPException
from connectors.checkmarx_api import CheckmarxAPI
from connectors.risksense_api import router as risksense_router
from core.orchestrator import GreenCorridorOrchestrator

app = FastAPI(title="Green Corridor API")

checkmarx_client = CheckmarxAPI(base_url="https://checkmarx.example.com/api", token="YOUR_TOKEN")
orchestrator = GreenCorridorOrchestrator(checkmarx_client)

app.include_router(risksense_router)

@app.get("/aggregate_vulnerabilities/{project_id}")
async def aggregate_vulnerabilities(project_id: int):
    try:
        data = orchestrator.aggregate_vulnerabilities(project_id)
        return {"project_id": project_id, "combined_vulnerabilities": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
