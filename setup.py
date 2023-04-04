from setuptools import setup, find_packages

with open("README.md", "r", encoding = "utf-8") as f:
    long_description = f.read()

setup(
    name = "pywebsoc",
    version = "0.0.12",
    author = "Ryan Lee, Anastacio Ruiz, Ernest Yao",
    author_email = "rhahnwoonglee@gmail.com",
    description = "UCI WebSoc API and Other Packages",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/printSANO/pywebsoc",
    project_urls = {
        "Bug Tracker": "https://github.com/printSANO/pywebsoc/issues",
        "repository": "https://github.com/printSANO/pywebsoc"
    },
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    package_dir = {"": "src"},
    packages = find_packages(where="src"),
    python_requires = ">=3.6",
    install_requires = [
        'beautifulsoup4>=4.11.1',
        'requests>=2.28.1'
    ]
)