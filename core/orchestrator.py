
from connectors.checkmarx_api import CheckmarxAPI
from connectors.risksense_api import mock_vulnerabilities

class GreenCorridorOrchestrator:
    def __init__(self, checkmarx_client: CheckmarxAPI):
        self.checkmarx = checkmarx_client
    
    def aggregate_vulnerabilities(self, project_id: int):
        cx_results = self.checkmarx.get_scan_results(project_id)
        combined = []
        combined.extend(cx_results.get("vulnerabilities", []))
        combined.extend(mock_vulnerabilities)
        # Simplified deduplication and risk scoring
        return combined
