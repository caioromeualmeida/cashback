
import uvicorn
from fastapi import FastAPI
from fastapi_pagination import add_pagination

from app.api.v1.api import api_router
from app.core import api_settings, server_settings
from app.core.database import create_client, free_client

app = FastAPI(
    title=api_settings.title,
    description=api_settings.description,
    version=api_settings.version,
    openapi_url=f"{api_settings.api_version_str}/openapi.json"
)


@app.on_event("startup")
async def startup_db_client():
    await create_client()


@app.on_event("shutdown")
async def shutdown_db_client():
    await free_client()

app.include_router(api_router, prefix=api_settings.api_version_str)

add_pagination(app)

if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host=server_settings.host,
        port=server_settings.port,
        reload=server_settings.reload
    )
