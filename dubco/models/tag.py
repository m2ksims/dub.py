from typing import Dict, Optional
from dubco.request import Request


class Tag:
    def __init__(self, project_slug: str) -> None:
        self.slug: str = project_slug

    def create(self, name: str) -> Optional[Dict]:
        """Create a new tag for the authenticated project.

        Parameters:
            name (str): The name of the tag to create.

        Returns:
            Optional[Dict]: A dictionary representing the JSON response, if available.
        """
        payload = {"tag": name}

        response = Request(
            method="POST", endpoint=f"projects/{self.slug}/tags", payload=payload
        ).execute()

        return response

    def get_all(self) -> Optional[Dict]:
        """Retrieve a list of tags for the authenticated project.

        Returns:
            Optional[Dict]: A dictionary representing the JSON response, if available.
        """
        response = Request(
            method="GET", endpoint=f"projects/{self.slug}/tags"
        ).execute()

        return response
