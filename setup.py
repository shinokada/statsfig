import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ndfig",
    version="0.1.0",
    author="Shinichi Okada",
    author_email="okada.shin@gmail.com",
    description="Normal Distribution Figures package.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shinokada/ndfig",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'matplotlib', 'numpy', 'scipy.stats'
    ],
    python_requires='>=3.6',
)
