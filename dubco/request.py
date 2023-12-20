import requests
import dubco
from dubco.errors import (
    AuthorizationError,
    NotFoundError,
    RateLimitExceededError,
    ServerError,
    DubException,
    BadRequest,
)
from typing import Dict, Optional
from ratelimit import limits, RateLimitException


class Request:
    def __init__(self, method: str, endpoint: str, payload: Optional[Dict[str, str]] = None):
        self.method = method
        self.endpoint = endpoint
        self.payload = payload
        self.base_url: str = "https://api.dub.co/"

    def execute(self) -> Dict:
        try:
            response = self._make_request()
        except RateLimitException:
            raise RateLimitExceededError(
                "You cannot make more than 10 calls per second, slow down."
            )

        possible_errors = {
            401: AuthorizationError("The request requires user authentication."),
            403: BadRequest(
                "The server understood the request, but refuses to authorize it."
            ),
            404: NotFoundError("The requested resource could not be found."),
            429: RateLimitExceededError("Too many requests."),
            500: ServerError(
                "The server encountered an unexpected condition which prevented it from fulfilling the request."
            ),
        }

        if response.status_code != 200:
            error = possible_errors.get(
                response.status_code,
                DubException(
                    f"Something went wrong and raised with status code {response.status_code}."
                ),
            )

            raise error

        return response.json()

    @limits(calls=10, period=1)
    def _make_request(self) -> requests.Response:
        headers = self.__headers
        method = self.method
        payload = self.payload
        url = self.base_url + self.endpoint

        try:
            return requests.request(
                method=method, url=url, headers=headers, json=payload
            )
        except requests.HTTPError as e:
            raise e

    @property
    def __headers(self) -> Dict:
        if not dubco.api_key:
            raise ValueError("You must provide an API key.")
        return {"Authorization": f"Bearer {dubco.api_key}"}
