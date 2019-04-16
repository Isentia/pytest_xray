from setuptools import setup


def long_description():
    with open("README.md") as f:
        return f.read()


setup(
    name="myproject",
    version="0.1.1",
    long_description=long_description(),
    packages=["myproject"],
    install_requires=["pytest"],
    summary="py.test Xray integration plugin, using markers",
    entry_points={"pytest11": ["pytest_xray = src.pytest_xray"]},
)

