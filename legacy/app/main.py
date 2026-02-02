import asyncio
import uvicorn
import structlog
from app.core.config import settings
from app.core.logging import setup_logging
from app.core.redis import redis_manager
from app.core.db import db_manager
from app.core.auth import init_firebase
from app.apps.public import create_public_app
from app.apps.parcel_internal import create_parcel_internal_app
from app.apps.party_internal import create_party_internal_app

# Initialize logging
setup_logging()
logger = structlog.get_logger()

async def run_servers():
    """Run Public, Parcel Internal, and Party Internal API servers concurrently."""
    
    # Initialize shared resources
    await redis_manager.connect()
    init_firebase()
    
    # Create all FastAPI applications
    public_app = create_public_app()
    parcel_internal_app = create_parcel_internal_app()
    party_internal_app = create_party_internal_app()
    
    # Configure uvicorn servers
    public_config = uvicorn.Config(
        public_app,
        host=settings.HOST,
        port=settings.PUBLIC_PORT,
        log_level=settings.LOG_LEVEL.lower(),
    )
    parcel_config = uvicorn.Config(
        parcel_internal_app,
        host=settings.HOST,
        port=settings.PARCEL_INTERNAL_PORT,
        log_level=settings.LOG_LEVEL.lower(),
    )
    party_config = uvicorn.Config(
        party_internal_app,
        host=settings.HOST,
        port=settings.PARTY_INTERNAL_PORT,
        log_level=settings.LOG_LEVEL.lower(),
    )
    
    public_server = uvicorn.Server(public_config)
    parcel_server = uvicorn.Server(parcel_config)
    party_server = uvicorn.Server(party_config)
    
    logger.info("servers_starting", 
                public_port=settings.PUBLIC_PORT, 
                parcel_port=settings.PARCEL_INTERNAL_PORT,
                party_port=settings.PARTY_INTERNAL_PORT)
    
    try:
        # Run all servers concurrently
        await asyncio.gather(
            public_server.serve(),
            parcel_server.serve(),
            party_server.serve(),
        )
    except Exception as e:
        logger.error("servers_failed", error=str(e))
    finally:
        # Cleanup shared resources
        await redis_manager.disconnect()
        await db_manager.disconnect()
        logger.info("servers_stopped")

if __name__ == "__main__":
    try:
        asyncio.run(run_servers())
    except KeyboardInterrupt:
        pass