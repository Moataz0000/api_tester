from setuptools import setup, find_packages

setup(
    name="api_tester",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests"
    ],
    entry_points={
        "console_scripts": [
            "api-tester=api_tester.cli:main"
        ]
    },
    author="Moataz Fawzy",
    description="A Python package to test API endpoints easily",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Moataz0000/api_tester",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
