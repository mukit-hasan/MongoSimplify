from setuptools import setup, find_packages


DESCRIPTION = 'MongoSimplify is a versatile Python library for easy and efficient MongoDB interaction.'

setup(
    name="MongoSimplify",
    version="0.5.0",
    author="Mukit Hasan",
    author_email="mukithasan58@gmail.com",
    description=DESCRIPTION,
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/mukit-hasan/MongoSimplify",
    packages=find_packages(),
    install_requires=[
        "pymongo",
    ],
    keywords=['python', 'pymongo', 'MongoSimplify', 'mongodb', 'nosql'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.11",
)
