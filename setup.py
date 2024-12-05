from setuptools import setup, find_packages

setup(
    name="sarthiai",
    version="1.0.1",
    description="Official Python SDK for SarthiAI API",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",  # README format
    url="https://github.com/SarthiAI/SarthiAI-Python-SDK",  # Link to GitHub repo or project homepage
    author="SarthiAI",
    author_email="contact@sarthiai.com", # Change this if needed
    packages=find_packages(),
    install_requires=["requests>=2.32.3", "pydantic>=2.9.2"],
    python_requires=">=3.9.12",
)
