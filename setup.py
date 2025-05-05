from setuptools import setup, find_packages

def read_version():
    with open("libml/VERSION") as f:
        return f.read().strip()

setup(
    name="libml",
    version=read_version(),
    description="Reusable preprocessing library for sentiment analysis",
    author="Gyum Cho",
    packages=find_packages(),
    install_requires=[
        "scikit-learn"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ],
    python_requires='>=3.6',
)
