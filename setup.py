import setuptools

__version__ = "0.0.3"

REPO_NAME = "qunix"

setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)