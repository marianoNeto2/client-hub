from fastapi import FastAPI

from app.routers.auth import router as auth_router
from app.routers.organization import router as organization_router
from app.routers.customer import router as customer_router
from app.routers.membership import router as membership_router
from app.routers.user import router as user_router

app = FastAPI()

app.include_router(organization_router)
app.include_router(customer_router)
app.include_router(membership_router)
app.include_router(user_router)
app.include_router(auth_router)
