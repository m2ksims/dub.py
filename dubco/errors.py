class DubException(BaseException):
    """Base exception for all exceptions raised by the `dubco` library."""


class AuthorizationError(DubException):
    """Raised for authorization-related errors."""

    pass


class RateLimitExceededError(DubException):
    """Raised when the rate limit for API requests is exceeded."""

    pass


class NotFoundError(DubException):
    """Raised when a requested resource is not found."""

    pass


class BadRequest(DubException):
    """Raised when the server refuses to authorize the request made."""

    pass


class ServerError(DubException):
    """Raised for general server errors."""

    pass
