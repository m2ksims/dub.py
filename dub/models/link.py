from typing import Dict, List, Optional
from dub.request import Request


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
    ) -> Dict:
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
            Dict: A dictionary representing the JSON response, if available.
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
            method="POST", endpoint="links", payload=payload, params=params
        ).execute()

        return response

    def get(self, domain: str, key: str) -> Dict:
        """Retrieve the info for a link from their domain and key.

        Parameters:
            domain (str): The domain of the link to retrieve. E.g. for dub.sh/github, the domain is 'dub.sh'.
            key (str): The key of the link to retrieve. E.g. for dub.sh/github, the key is 'github'.

        Returns:
            Dict: A dictionary representing the JSON response, if available.
        """
        params = {"projectSlug": self.slug, "domain": domain, "key": key}

        response = Request(method="GET", endpoint="links/info", params=params).execute()

        return response

    def delete(self, link_id: str) -> Dict:
        """Delete a link for the authenticated project.

        Parameters:
            link_id (str): The id of the link to delete.

        Returns:
            Dict: A dictionary representing the JSON response, if available.
        """
        params = {"projectSlug": self.slug}
        response = Request(
            method="DELETE", endpoint=f"links/{link_id}", params=params
        ).execute()

        return response

    def edit(self, link_id: str, **payload) -> Dict:
        """Edit a link for the authenticated project.

        Parameters:
            link_id (str): The id of the link to edit.
            **payload (dict): A dictionary containing properties to edit in the link - the same properties as creating a link.

        Returns:
            Dict: A dictionary representing the JSON response, if available.
        """
        params = {"projectSlug": self.slug}
        response = Request(
            method="PUT", endpoint=f"links/{link_id}", params=params, payload=payload
        ).execute()

        return response

    def get_links(
        self,
        page: Optional[int] = 1,
        domain: Optional[str] = None,
        tag_id: Optional[str] = None,
        search: Optional[str] = None,
        sort: Optional[str] = "createdAt",
        user_id: Optional[str] = None,
        show_archived: Optional[bool] = False,
    ) -> List[Dict]:
        """Retrieve a list of links for the authenticated project.

        Parameters:
            page (Optional[int]): The page number for pagination (each page contains 100 links).
            domain (Optional[str]): The domain to filter the links by. E.g. 'ac.me'. If not provided, all links for the project will be returned.
            tag_id (Optional[str]): The tag ID to filter the links by.
            search (Optional[str]): The search term to filter the links by. The search term will be matched against the short link slug and the destination url.
            sort (Optional[str]): The field to sort the links by. The default is `createdAt`, and sort order is always descending. Available options: `createdAt`, `clicks`, `lastClicked`.
            user_id (Optional[str]): The user ID to filter the links by.
            show_archived (Optional[bool]): Whether to include archived links in the response.

        Returns:
            List[Dict]: A list of dictionaries representing the JSON response, if available.
        """
        params = {
            "projectSlug": self.slug,
            "domain": domain,
            "tagId": tag_id,
            "search": search,
            "sort": sort,
            "page": page,
            "userId": user_id,
            "showArchived": show_archived,
        }

        response = Request(method="GET", endpoint="links", params=params).execute()

        return response

    def bulk_create(self, payload: List[Dict]) -> List[Dict]:
        """Bulk create up to 100 links for the authenticated project.

        Find more information about this method here: https://dub.co/docs/api-reference/endpoint/bulk-create-links

        Parameters:
            payload (List[Dict]): A list of dictionaries containing link information.

        Returns:
            List[Dict]: A list of dictionaries representing the JSON response, if available.
        """
        params = {"projectSlug": self.slug}

        response = Request(
            method="POST", endpoint="links/bulk", params=params, payload=payload
        ).execute()

        return response
