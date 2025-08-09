# Green Corridor Backend

## Overview
Green Corridor is a unified platform backend connecting Azure DevOps, Checkmarx, SonarQube, Fortify, RiskSense (mock), ServiceNow CMDB, and Splunk SIEM via APIs to orchestrate vulnerability management workflows.

## Setup

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Set environment variables for API tokens and URLs (e.g., CHECKMARX_TOKEN, ADO_TOKEN).

3. Run FastAPI server:
   ```
   uvicorn api.main:app --reload
   ```

## Usage

- Access aggregated vulnerabilities endpoint:
  ```
  GET /aggregate_vulnerabilities/{project_id}
  ```

- Mock RiskSense vulnerabilities available at:
  ```
  GET /risksense/vulnerabilities
  ```