"""Packaging configuration for editable installs."""

from setuptools import find_packages, setup


setup(
    name="medical-chatbot",
    version="0.1.0",
    description="Medical chatbot project scaffold.",
    packages=find_packages(include=["src", "src.*"]),
    python_requires=">=3.10,<3.13",
)
