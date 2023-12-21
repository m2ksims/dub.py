"""
A simple & easy to use python wrapper built around the dub.co API. 

Copyright (c) 2023 Maksims K.
License: MIT
"""
from dubco.models.tag import Tag
from dubco.models.project import Project
from dubco.models.link import Link

api_key: str = None

__all__ = [
    "Tag",
    "Project",
    "Link",
]
