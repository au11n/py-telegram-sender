from setuptools import setup, find_packages


setup(
    name="py-telegram-sender",
    version="0.1.3",
    author="Nikita Aull",
    author_email="aull.nikita.i@gmail.com",
    description="A simple library for sending messages and files via Telegram",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/au11n/py-telegram-sender",
    packages=find_packages(),
    install_requires=["requests"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    
    python_requires=">=3.6",
)