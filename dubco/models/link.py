from typing import Dict, Optional
from dubco.request import Request


class Link:
    def __init__(self, slug: str) -> None:
        """Initialize a new Project class.

        Parameters:
            slug (str): The slug for the project to create, retrieve, delete and update links. E.g. for app.dub.co/acme, the projectSlug is 'acme'.
        """
        self.slug = slug

    def create(
        self,
        domain: str,
        destination_url: str,
        key: Optional[str] = None,
        archived: Optional[bool] = False,
        expires_at: Optional[str] = None,
        password: Optional[str] = None,
        proxy: Optional[bool] = False,
        title: Optional[str] = None,
        description: Optional[str] = None,
        image: Optional[str] = None,
        rewrite: Optional[bool] = False,
        ios: Optional[str] = None,
        android: Optional[str] = None,
        geo: Optional[Dict] = None,
        public_stats: Optional[bool] = False,
        tag_id: Optional[str] = None,
        comments: Optional[str] = None,
    ) -> Optional[Dict]:
        """Create a new link for the authenticated project.

        Parameters:
            slug (str): The slug for the project to create links for. E.g. for app.dub.co/acme, the projectSlug is 'acme'.
            domain (str): The domain of the short link.
            destination_url (str): The destination URL of the short link.
            key (Optional[str]): The short link slug. If not provided, a random 7-character slug will be generated.
            archived (Optional[bool]): Whether the short link is archived.
            expires_at (Optional[str]): The date and time when the short link will expire in ISO-8601 format. Must be in the future.
            password (Optional[str]): The password required to access the destination URL of the short link.
            proxy (Optional[bool]): Whether the short link uses Custom Social Media Cards feature.
            title (Optional[str]): The title of the short link generated via api.dub.co/metatags. Will be used for Custom Social Media Cards if `proxy` is true.
            description (Optional[str]): The description of the short link generated via api.dub.co/metatags. Will be used for Custom Social Media Cards if `proxy` is true.
            image (Optional[str]): The image of the short link generated via api.dub.co/metatags. Will be used for Custom Social Media Cards if `proxy` is true.
            rewrite (Optional[bool]): Whether the short link uses link cloaking.
            ios (Optional[str]): The iOS destination URL for the short link for iOS device targeting.
            android (Optional[str]): The Android destination URL for the short link for Android device targeting.
            geo (Optional[Dict]): Geo targeting information for the short link in JSON format {[COUNTRY]: "https://example.com" }. Learn more: https://dub.sh/geo
            public_stats (Optional[bool]): Whether the short link's stats are publicly accessible.
            tag_id (Optional[str]): The unique id of the tag assigned to the short link.
            comments (Optional[str]): The comments for the short link.

        Returns:
            Optional[Dict]: A dictionary representing the JSON response, if available.
        """
        params = {"projectSlug": self.slug}
        payload = {
            "domain": domain,
            "url": destination_url,
            "key": key,
            "archived": archived,
            "expiresAt": expires_at,
            "password": password,
            "proxy": proxy,
            "title": title,
            "description": description,
            "image": image,
            "rewrite": rewrite,
            "ios": ios,
            "android": android,
            "geo": geo,
            "publicStats": public_stats,
            "tagId": tag_id,
            "comments": comments,
        }

        response = Request(
            method="POST", endpoint=f"links", payload=payload, params=params
        ).execute()

        return response

    def get(self, domain: str, key: str) -> Optional[Dict]:
        """Retrieve the info for a link from their domain and key.

        Parameters:
            domain (str): The domain of the link to retrieve. E.g. for dub.sh/github, the domain is 'dub.sh'.
            key (str): The key of the link to retrieve. E.g. for dub.sh/github, the key is 'github'.

        Returns:
            Optional[Dict]: A dictionary representing the JSON response, if available.
        """
        params = {"projectSlug": self.slug, "domain": domain, "key": key}

        response = Request(
            method="GET", endpoint=f"links/info", params=params
        ).execute()

        return response

    # TODO:
    # PUT (Edit a Link) -> Edit a link for the authenticated project.
    # DEL (Delete a Link) -> Delete a link for the authenticated project
    # GET (Retrieve a list of links) -> Retrieve a list of links for the authenticated project. The list will be paginated and the provided query parameters allow filtering the returned links.
    # POST (Bulk create links) -> Bulk create up to 100 links for the authenticated project.
