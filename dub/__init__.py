"""
A simple & easy to use python wrapper built around the dub.co API. 

Copyright (c) 2023 Maksims K.
License: MIT
"""
from dub.models.tag import Tag
from dub.models.project import Project
from dub.models.link import Link

api_key: str = None

__all__ = [
    "Tag",
    "Project",
    "Link",
]
