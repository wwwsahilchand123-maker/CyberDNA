import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

class Settings:
    APP_NAME = "CyberDNA"
    APP_VERSION = "1.0.0"
    ENV = os.getenv("APP_ENV", "development")
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./cyberdna.db")
    UPLOAD_DIR = Path(os.getenv("UPLOAD_DIR", "./uploads")).resolve()
    REPORTS_DIR = Path(os.getenv("REPORTS_DIR", "./reports")).resolve()
    MAX_UPLOAD_MB = int(os.getenv("MAX_UPLOAD_MB", "50"))
    MAX_UPLOAD_BYTES = MAX_UPLOAD_MB * 1024 * 1024
    CORS_ORIGINS = [o.strip() for o in os.getenv("CORS_ORIGINS", "http://localhost:5173").split(",")]
    AI_PROVIDER = os.getenv("AI_PROVIDER", "deterministic")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
    SECRET_KEY = os.getenv("SECRET_KEY", "change-me")
    ALLOWED_EXTENSIONS = {".log",".txt",".csv",".json",".zip",".docx",".pdf",".png",".jpg",".jpeg",".db",".sqlite",".raw",".evtx",".pcap",".xml"}

settings = Settings()
settings.UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
settings.REPORTS_DIR.mkdir(parents=True, exist_ok=True)
