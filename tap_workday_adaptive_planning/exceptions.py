class WorkdayAdaptivePlanningError(Exception):
    """class representing Generic Http error."""

    def __init__(self, message=None, response=None):
        super().__init__(message)
        self.message = message
        self.response = response


class WorkdayAdaptivePlanningBackoffError(WorkdayAdaptivePlanningError):
    """class representing backoff error handling."""
    pass

class WorkdayAdaptivePlanningBadRequestError(WorkdayAdaptivePlanningError):
    """class representing 400 status code."""
    pass

class WorkdayAdaptivePlanningUnauthorizedError(WorkdayAdaptivePlanningError):
    """class representing 401 status code."""
    pass


class WorkdayAdaptivePlanningForbiddenError(WorkdayAdaptivePlanningError):
    """class representing 403 status code."""
    pass

class WorkdayAdaptivePlanningNotFoundError(WorkdayAdaptivePlanningError):
    """class representing 404 status code."""
    pass

class WorkdayAdaptivePlanningConflictError(WorkdayAdaptivePlanningError):
    """class representing 409 status code."""
    pass

class WorkdayAdaptivePlanningUnprocessableEntityError(WorkdayAdaptivePlanningBackoffError):
    """class representing 422 status code."""
    pass

class WorkdayAdaptivePlanningRateLimitError(WorkdayAdaptivePlanningBackoffError):
    """class representing 429 status code."""
    pass

class WorkdayAdaptivePlanningInternalServerError(WorkdayAdaptivePlanningBackoffError):
    """class representing 500 status code."""
    pass

class WorkdayAdaptivePlanningNotImplementedError(WorkdayAdaptivePlanningBackoffError):
    """class representing 501 status code."""
    pass

class WorkdayAdaptivePlanningBadGatewayError(WorkdayAdaptivePlanningBackoffError):
    """class representing 502 status code."""
    pass

class WorkdayAdaptivePlanningServiceUnavailableError(WorkdayAdaptivePlanningBackoffError):
    """class representing 503 status code."""
    pass

ERROR_CODE_EXCEPTION_MAPPING = {
    400: {
        "raise_exception": WorkdayAdaptivePlanningBadRequestError,
        "message": "A validation exception has occurred."
    },
    401: {
        "raise_exception": WorkdayAdaptivePlanningUnauthorizedError,
        "message": "The access token provided is expired, revoked, malformed or invalid for other reasons."
    },
    403: {
        "raise_exception": WorkdayAdaptivePlanningForbiddenError,
        "message": "You are missing the following required scopes: read"
    },
    404: {
        "raise_exception": WorkdayAdaptivePlanningNotFoundError,
        "message": "The resource you have specified cannot be found."
    },
    409: {
        "raise_exception": WorkdayAdaptivePlanningConflictError,
        "message": "The API request cannot be completed because the requested operation would conflict with an existing item."
    },
    422: {
        "raise_exception": WorkdayAdaptivePlanningUnprocessableEntityError,
        "message": "The request content itself is not processable by the server."
    },
    429: {
        "raise_exception": WorkdayAdaptivePlanningRateLimitError,
        "message": "The API rate limit for your organisation/application pairing has been exceeded."
    },
    500: {
        "raise_exception": WorkdayAdaptivePlanningInternalServerError,
        "message": "The server encountered an unexpected condition which prevented" \
            " it from fulfilling the request."
    },
    501: {
        "raise_exception": WorkdayAdaptivePlanningNotImplementedError,
        "message": "The server does not support the functionality required to fulfill the request."
    },
    502: {
        "raise_exception": WorkdayAdaptivePlanningBadGatewayError,
        "message": "Server received an invalid response."
    },
    503: {
        "raise_exception": WorkdayAdaptivePlanningServiceUnavailableError,
        "message": "API service is currently unavailable."
    }
}

