# Simple example of URL versioning in FastAPI

## Setup
Needs a python environment with FastAPI installed.
On Linux or Mac can typically use the following commands to create an environment and start the app:
```
python3 -m venv venv
source venv/bin/activate
pip install "fastapi[standard]"
fastapi dev
```

## Usage
When running:
- http://127.0.0.1:8000/docs shows API docs
- http://127.0.0.1:8000/now shows the current time
- http://127.0.0.1:8000/v1/now also shows the current time
- http://127.0.0.1:8000/v2/now shows the current time and timezone
- http://127.0.0.1:8000/latest/now also shows the current time and timezone
