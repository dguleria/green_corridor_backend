# Architecture Overview

## Components

- **Connectors**: Modular API clients for integrating with external systems like Checkmarx, SonarQube, Fortify, RiskSense (mock), ServiceNow CMDB, Splunk SIEM, and Azure DevOps.
- **Core**: Orchestrator module that aggregates vulnerability data and implements business logic for risk prioritization and remediation workflows.
- **API**: FastAPI application exposing REST endpoints consumed by frontend applications or other services.
- **Docs**: Setup, usage, and architecture documentation to assist developers and users.

## Workflow

1. Fetch vulnerability data from multiple scanning tools and risk platforms.
2. Aggregate and deduplicate vulnerabilities, applying risk scoring and business context.
3. Provide unified views via API endpoints for dashboards and reporting.
4. Enable automation of remediation ticket creation and risk acceptance through integrations with CMDB and DevOps tools.