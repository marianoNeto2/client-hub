from fastapi import FastAPI
from app.routers.auth import router as auth_router
from app.routers.organization import router as organization_router
from app.routers.customer import router as customer_router
from app.routers.membership import router as membership_router
from app.routers.user import router as user_router
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

limiter = Limiter(key_func=get_remote_address)

app = FastAPI()

app.include_router(organization_router)
app.include_router(customer_router)
app.include_router(membership_router)
app.include_router(user_router)
app.include_router(auth_router)

app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)