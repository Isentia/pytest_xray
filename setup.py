from setuptools import setup, find_packages


def long_description():
    with open("README.md") as f:
        return f.read()


def pkg_install_requires():
    with open("requirements.txt") as f:
        results = f.read()
        return results.split("\n")


setup(
    name="pytest_xray",
    version="0.1.6",
    long_description=long_description(),
    packages=find_packages(exclude=("tests",)),
    install_requires=pkg_install_requires(),
    summary="py.test Xray integration plugin, using markers",
    entry_points={"pytest11": ["pytest_xray = pytest_xray.plugin"]},
)

