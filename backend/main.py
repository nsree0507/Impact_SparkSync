from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import API routers
from backend.api.location_routes import router as location_router
from backend.api.customer_routes import router as customer_router
from backend.api.admin_routes import router as admin_router

# Import logger
from backend.utils.logger import log_event


# -----------------------------
# FastAPI App Initialization
# -----------------------------
app = FastAPI(
    title="AI-Driven Geofencing Retail Offer Recommendation System",
    description="Smart retail marketing system using AI recommendations, POS data, and geofencing.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)


# -----------------------------
# Enable CORS (for future React frontend)
# -----------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# -----------------------------
# Register API Routers
# -----------------------------
app.include_router(
    location_router,
    prefix="/location",
    tags=["Location Services"]
)

app.include_router(
    customer_router,
    prefix="/customer",
    tags=["Customer Services"]
)

app.include_router(
    admin_router,
    prefix="/admin",
    tags=["Admin Services"]
)


# -----------------------------
# Root Endpoint
# -----------------------------
@app.get("/")
def home():
    return {
        "system": "AI Retail Recommendation System",
        "status": "Running",
        "documentation": "/docs"
    }


# -----------------------------
# Health Check Endpoint
# -----------------------------
@app.get("/health")
def health_check():
    return {
        "status": "API running successfully"
    }


# -----------------------------
# Startup Event
# -----------------------------
@app.on_event("startup")
def startup_event():
    log_event("Smart Retail AI System Started")


# -----------------------------
# Shutdown Event
# -----------------------------
@app.on_event("shutdown")
def shutdown_event():
    log_event("Smart Retail AI System Stopped")