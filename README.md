Project Overview: Auto Test Generation Pipeline (A → B)

This prototype demonstrates a CI/CD workflow that automatically detects new API endpoints, generates tests with an AI model, and executes them on GitHub Actions.

A (app-repo)  FastAPI-based application exposing endpoints like /ping, /greet/{name}, /sum, etc.
B (b-tests)   CI pipeline that listens to repository_dispatch events from A, generates tests using Google Gemini, and executes them with pytest.

1.	A-repo push → triggers workflow
	•	When a new commit is pushed to A’s main branch,
the workflow Diff to Tests compares changes (git diff) using GitHub REST API.
2.	Endpoint Extraction
	•	A custom Python script (scripts/extract_endpoints.py) parses changed .py files and extracts FastAPI routes.
3.	Event Dispatch to B
	•	The extracted endpoints are sent as JSON payload via GitHub REST API to B
4.	B-repo receives the event
	•	The workflow Generate & Run Tests is triggered automatically by the repository_dispatch event.
5.	Test Generation with Gemini
	•	B executes scripts/generate_tests_with_gemini.py, which:
	•	Reads payload.json
	•	Builds a context-aware prompt
	•	Calls Google Gemini 2.5 Flash via google-generativeai
	•	Generates a valid pytest file
6.	Application Spin-up
	•	The workflow clones the latest version of app-repo,
installs dependencies, and runs the app on port 8000 via uvicorn.
7.	Pytest Execution
	•	The generated test suite is executed against the live API, and results are visible in the workflow summary.
8.	Artifact Upload
	•	The generated test file is saved under tests/generated/ and uploaded as a GitHub Actions artifact for traceability.
