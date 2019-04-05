from setuptools import setup

setup(
    name="myproject",
    packages=["myproject"],
    install_requires=["pytest"],
    summary="py.test Xray integration plugin, using markers",
    entry_points={"pytest11": ["pytest_xray = src.pytest_xray"]},
)

