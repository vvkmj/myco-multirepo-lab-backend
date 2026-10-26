# Myco Multirepo Lab — Backend Service

FastAPI-powered telemetry and status service for the distributed multi-repository lab.

## Architecture & Relationships

This service is one part of a multi-repository distributed system:
- Consumed by the web UI in [myco-multirepo-lab-frontend](https://github.com/vvkmj/myco-multirepo-lab-frontend).
- Deployed and routed via manifests in [myco-multirepo-lab-k8s](https://github.com/vvkmj/myco-multirepo-lab-k8s).

## Local Development & Testing

```bash
# Run tests
pytest tests/

# Run service locally
uvicorn app.main:app --host 0.0.0.0 --port 8080
```
