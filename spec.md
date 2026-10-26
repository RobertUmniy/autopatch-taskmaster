# Technical Specification - AutoPatch AI

## Architecture Overview
AutoPatch AI follows an agentic pipeline architecture:
`Log Listener / API Gateway -> LLM Agent Engine -> Patch Formatter -> Web UI / Git Integration`

## Tech Stack
- **Frontend**: React, Tailwind CSS, Framer Motion
- **Backend / Agent Core**: Node.js / Python with LLM integration
- **Version Control**: Git / GitHub API integration

## Security & Reliability
- Read-only access to log streams.
- Human-in-the-loop verification before applying patches to master branches.
