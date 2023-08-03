from setuptools import setup, find_packages

setup(
    name="telebirrTxChecker",
    version="0.0.2",
    packages=find_packages(),
    url="https://github.com/wizkiye/TelebirrPaymentProcessor",
    license="MIT",
    author="Kidus",
    author_email="wizkiye@gmail.com",
    description="asynchronous telebirr transaction checker",
    install_requires=[
        "httpx>=0.24.1",
        "bs4>=0.0.1",
        "beautifulsoup4>=4.12.2",
        "pdfkit>=1.0.0",
    ],
)
