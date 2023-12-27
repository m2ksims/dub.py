from typing import Dict
from dub.request import Request


class Project:
    def __init__(self) -> None:
        """Initialize a new Project class."""
        pass

    @classmethod
    def get(self, slug: str) -> Dict:
        """Retrieve a project for the authenticated user.

        Parameters:
            slug (str): The slug for the project to retrieve. E.g. for app.dub.co/acme, the projectSlug is 'acme'.

        Returns:
            Dict: A dictionary representing the JSON response, if available.
        """
        response = Request(method="GET", endpoint=f"projects/{slug}").execute()

        return response

    @classmethod
    def get_all(self) -> Dict:
        """Retrieve a list of projects for the authenticated user.

        Returns:
            Dict: A dictionary representing the JSON response, if available.
        """
        response = Request(method="GET", endpoint="projects").execute()

        return response
