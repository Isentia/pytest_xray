from setuptools import setup

setup(
    name="myproject",
    version="0.1"
    packages=["myproject"],
    install_requires=["pytest"],
    summary="py.test Xray integration plugin, using markers",
    entry_points={"pytest11": ["pytest_xray = src.pytest_xray"]},
)

