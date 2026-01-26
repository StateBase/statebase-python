from setuptools import setup, find_packages

setup(
    name="statebase-sdk",
    version="0.1.0",
    description="Python SDK for StateBase API",
    author="StateBase Team",
    packages=find_packages(),
    install_requires=[
        "httpx>=0.24.0",
        "pydantic>=2.0.0",
        "typing-extensions>=4.0.0"
    ],
    python_requires=">=3.8",
)
