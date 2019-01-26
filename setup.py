from setuptools import find_packages, setup

from mangum.__version__ import __version__


def get_long_description():
    return open("README.md", "r", encoding="utf8").read()


setup(
    name="mangum",
    version=__version__,
    packages=find_packages(),
    license="MIT",
    url="https://github.com/erm/mangum",
    description="ASGI serverless adapters",
    long_description=get_long_description(),
    extras_require={"full": ["azure-functions", "boto3", "click"]},
    long_description_content_type="text/markdown",
    entry_points={"console_scripts": ["mangum = mangum.__main__:main"]},
    author="Jordan Eremieff",
    author_email="jordan@eremieff.com",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
)
