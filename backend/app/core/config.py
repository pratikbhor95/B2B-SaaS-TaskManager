import os 
from dotenv import load_dotenv

load_dotenv()

class Config:
    CLERK_SECRET_KEY = os.getenv("CLERK_SECRET_KEY", "")
    CLERK_PUBLISHABLE_KEY = os.getenv("CLERK_PUBLISHABLE_KEY", "")
    CLERK_JWKS_URL = os.getenv("CLERK_JWKS_URL", "")
    CLERK_WEBHOOK_SECRET = os.getenv("CLERK_WEBHOOK_SECRET", "")

    DATABASE_URL = os.getenv("DATABASE_URL", "")
    FRONTEND_URL = os.getenv("FRONTEND_URL", "")

    FREE_TIER_MEMBERSHIP_LIMIT: int = 2
    PRO_TIER_MEMBERSHIP_LIMIT = 0  # unlimited

    PROJECT_NAME = os.getenv("PROJECT_NAME", "Task Management API")
    PROJECT_VERSION = os.getenv("PROJECT_VERSION", "1.0.0")
    PROJECT_DESCRIPTION = os.getenv("PROJECT_DESCRIPTION", "B2B Task Board App")

settings = Config()