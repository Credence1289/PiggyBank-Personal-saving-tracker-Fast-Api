from sqlalchemy import create_engine
from app.core.config import settings
import logging

logger = logging.getLogger(__name__)

DB_URL = str(settings.DB_URL)

if not DB_URL:
    logger.critical("DB_URL environment variable not set")
    raise RuntimeError("DB_URL is not set")

engine = create_engine(
    DB_URL,
    echo=False
)
