from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from app.routers.auth import router as auth_router
from app.routers.organization import router as organization_router
from app.routers.customer import router as customer_router
from app.routers.membership import router as membership_router
from app.routers.user import router as user_router
from app.schemas.error import ErrorDetail, ErrorResponse
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded

from app.core.limiter import limiter

app = FastAPI()

app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

app.include_router(organization_router)
app.include_router(customer_router)
app.include_router(membership_router)
app.include_router(user_router)
app.include_router(auth_router)

def http_exception_handler(request: Request, exc: HTTPException):
    error = ErrorResponse(
        error=ErrorDetail(
            code=exc.status_code,
            message=str(exc.detail),
            details=None,
        )
    )
    return JSONResponse(status_code=exc.status_code, content=error.model_dump())

app.add_exception_handler(HTTPException, http_exception_handler)
