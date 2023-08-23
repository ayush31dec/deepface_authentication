from setuptools import find_packages, setup

# Declaring variables for setup functions
PROJECT_NAME = "DeepFace Authentication System"
VERSION = "0.0.1"
AUTHOR = "Ayush gupta"
DESRCIPTION = "This is a Face Authenticator Project"


setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESRCIPTION,
    packages=find_packages(),
)
