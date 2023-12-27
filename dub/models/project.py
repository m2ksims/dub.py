from typing import Dict, Optional
from dub.request import Request


class Project:
    def __init__(self) -> None:
        """Initialize a new Project class."""
        pass

    @classmethod
    def get(self, slug: str) -> Optional[Dict]:
        """Retrieve a project for the authenticated user.

        Parameters:
            slug (str): The slug for the project to retrieve. E.g. for app.dub.co/acme, the projectSlug is 'acme'.

        Returns:
            Optional[Dict]: A dictionary representing the JSON response, if available.
        """
        response = Request(method="GET", endpoint=f"projects/{slug}").execute()

        return response

    @classmethod
    def get_all(self) -> Optional[Dict]:
        """Retrieve a list of projects for the authenticated user.

        Returns:
            Optional[Dict]: A dictionary representing the JSON response, if available.
        """
        response = Request(method="GET", endpoint=f"projects").execute()

        return response
