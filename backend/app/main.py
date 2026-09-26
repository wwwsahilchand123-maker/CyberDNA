from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import time

from app.core.config import settings
from app.core.database import Base, engine
from app.core.logging_config import logger
from app.api import evidence, artifacts, timeline, findings, investigations, graph, ai, reports, dashboard, demo, search

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="CyberDNA API",
    description="AI-Powered Digital Forensics Investigation & Evidence Analysis Platform",
    version=settings.APP_VERSION,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def log_requests(request: Request, call_next):
    start = time.time()
    try:
        response = await call_next(request)
    except Exception as exc:
        logger.error(f"Unhandled error on {request.url.path}: {exc}")
        return JSONResponse(status_code=500, content={"detail": "Internal server error. Please contact the system administrator."})
    duration = round((time.time() - start) * 1000, 2)
    logger.info(f"{request.method} {request.url.path} -> {response.status_code} ({duration}ms)")
    return response

app.include_router(demo.router)
app.include_router(dashboard.router)
app.include_router(evidence.router)
app.include_router(artifacts.router)
app.include_router(timeline.router)
app.include_router(findings.router)
app.include_router(investigations.router)
app.include_router(graph.router)
app.include_router(ai.router)
app.include_router(reports.router)
app.include_router(search.router)

@app.get("/")
def root():
    return {"service": "CyberDNA API", "status": "operational", "version": settings.APP_VERSION}

@app.get("/health")
def health():
    return {"status": "ok"}
