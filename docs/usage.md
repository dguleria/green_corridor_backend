# Usage Guide

## Aggregated Vulnerabilities
- Endpoint: `/aggregate_vulnerabilities/{project_id}`
- Returns combined vulnerability data from Checkmarx and RiskSense (mock).

## RiskSense Mock API
- Endpoint: `/risksense/vulnerabilities`
- Returns sample vulnerabilities data for demonstration.

## Extend Connectors
- Add API token and URL configurations in respective connector files.
- Implement additional methods to fetch more detailed data as needed.

## Running the Server
- Use uvicorn to run the FastAPI server with hot reload for development.