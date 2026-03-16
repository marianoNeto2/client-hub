from contextlib import asynccontextmanager

from fastapi import FastAPI

import app.models  # noqa: F401
from app.core.database import Base, engine
from app.routers.auth import router as auth_router
from app.routers.organization import router as organization_router
from app.routers.customer import router as customer_router
from app.routers.membership import router as membership_router
from app.routers.user import router as user_router

@asynccontextmanager
async def lifespan(_: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(organization_router)
app.include_router(customer_router)
app.include_router(membership_router)
app.include_router(user_router)
app.include_router(auth_router)
