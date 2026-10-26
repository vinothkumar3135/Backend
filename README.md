# Practice Backend (FastAPI)

A small layered FastAPI app for practicing deployment: Docker, Jenkins CI/CD, cloud VMs.

## Run locally
    python3 -m venv venv && . venv/bin/activate
    pip install -r requirements.txt
    python server.py          # http://localhost:8000/docs

## Test
    pytest -q

## Docker
    docker build -t practice-backend .
    docker run -p 8000:8000 --env-file .env practice-backend

## Endpoints
- GET /health
- POST /api/auth/register, POST /api/auth/login
- GET/POST /api/businesses, GET/DELETE /api/businesses/{id} (Bearer token)

## Practice ideas
1. Push to GitHub, wire up the Jenkinsfile on an EC2 instance
2. Push the image to ECR/Docker Hub, deploy on ECS or a VM
3. Swap SQLite for Postgres (set DATABASE_URL) via docker-compose
4. Add Nginx + HTTPS, then Terraform the infra
