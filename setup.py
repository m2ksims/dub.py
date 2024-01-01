from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="dub.py",
    version="v1.0.3",
    author="Maksims K.",
    author_email="contact@maksims.co.uk",
    description="🔗 A python wrapper built around the dub.co API. ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/m2ksims/dub.py",
    packages=find_packages(),
    install_requires=["requests", "ratelimit"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
)
