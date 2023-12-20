# dubco.py

A wrapper built around the [dub.co API](https://dub.co/docs/api-reference/introduction) written in python.

## Installation
```
$ pip install dubco
```

## Usage
```py
import dubco

dubco.api_key = "API_KEY_HERE"

tag = dubco.Tag(slug="project")
tag.create(name="tag_name")
```