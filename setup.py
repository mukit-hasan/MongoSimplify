from setuptools import setup, find_packages

setup(
    name="PyMongoModel",
    version="0.1.0",
    author="Mukit Hasan",
    author_email="mukithasan58@gmail.com.com",
    description="A Python library for MongoDB integration with Django-like models",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/my_library",
    packages=find_packages(),
    install_requires=[
        "pymongo",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.11",
)
