from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines

setup(
    name = "GEN-CRAFTER",
    version = 0.1,
    author = "Harsha",
    packages = find_packages(),
    install_requires = requirements
)