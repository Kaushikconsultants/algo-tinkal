from fastapi import FastAPI, Depends, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
import os
from database import get_db, Trade
import urllib.parse

app = FastAPI(title="Upstox Algo Trading API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/health")
def health_check(db: Session = Depends(get_db)):
    # Test DB connection
    trade_count = db.query(Trade).count()
    return {"status": "healthy", "message": "Upstox Algo platform is running!", "trades_in_db": trade_count}

@app.get("/api/upstox/login")
def get_upstox_login_url():
    client_id = os.getenv("UPSTOX_API_KEY", "")
    redirect_uri = os.getenv("UPSTOX_REDIRECT_URI", "http://127.0.0.1:8000/callback")
    url = f"https://api.upstox.com/v2/login/authorization/dialog?response_type=code&client_id={client_id}&redirect_uri={urllib.parse.quote(redirect_uri)}"
    return {"login_url": url}

# Serve static files from React build
if os.path.exists("../frontend/dist"):
    app.mount("/assets", StaticFiles(directory="../frontend/dist/assets"), name="assets")

    @app.get("/{full_path:path}")
    async def serve_frontend(full_path: str):
        index_file = "../frontend/dist/index.html"
        if os.path.exists(index_file):
            return FileResponse(index_file)
        return {"error": "Frontend not built yet."}
