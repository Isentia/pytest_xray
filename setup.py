from setuptools import setup, find_packages
import os

XRAY_SETUP_DIR = os.path.abspath(os.path.dirname(__file__))


def long_description():
    filepath = os.path.join(XRAY_SETUP_DIR, "README.md")
    with open(filepath) as f:
        return f.read()


def pkg_install_requires():
    filepath = os.path.join(XRAY_SETUP_DIR, "requirements.txt")
    with open(filepath) as f:
        results = f.read()
        return results.split("\n")


setup(
    name="pytest_xray",
    author="Neville Tummon",
    author_email="nt.devs@gmail.com",
    version="0.1.7",
    python_requires=">=3.6.6",
    long_description=long_description(),
    packages=find_packages(exclude=("tests",)),
    download_url="https://github.com/Isentia/pytest_xray/archive/v0.1.7.tar.gz",
    install_requires=pkg_install_requires(),
    summary="py.test Xray integration plugin, using markers",
    entry_points={"pytest11": ["pytest_xray = pytest_xray.plugin"]},
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        "Development Status :: 3 - Alpha",
        # Indicate who your project is intended for
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Testing",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
)

