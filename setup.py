from setuptools import setup, find_packages


def long_description():
    with open("README.md") as f:
        return f.read()


setup(
    name="myproject",
    version="0.1.2",
    long_description=long_description(),
    packages=find_packages(exclude=("tests",)),
    install_requires=["pytest"],
    summary="py.test Xray integration plugin, using markers",
    entry_points={"pytest11": ["pytest_xray = src.pytest_xray"]},
)

