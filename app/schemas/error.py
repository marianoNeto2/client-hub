class ErrorDetail:
    code: int
    message: str
    details: str | None = None

class ErrorResponse:
    error: ErrorDetail