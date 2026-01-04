"""Setup script for Econometrics Agent."""

from setuptools import setup, find_packages
from pathlib import Path

# Read the README file
readme_file = Path(__file__).parent / "README.md"
long_description = readme_file.read_text() if readme_file.exists() else ""

setup(
    name="econometrics-agent",
    version="0.1.1",
    description="AI-powered econometrics agent for applied microeconometrics research",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Your Name",
    url="https://github.com/yourusername/econometrics-agent",
    packages=find_packages(),
    install_requires=[
        "pandas>=2.0.0",
        "numpy>=1.24.0",
        "statsmodels>=0.14.0",
        "scipy>=1.10.0",
        "matplotlib>=3.7.0",
        "seaborn>=0.12.0",
        "linearmodels>=5.0.0",
        "scikit-learn>=1.3.0",
        "pyarrow>=14.0.0",
        "sentence-transformers>=2.2.0",
    ],
    python_requires=">=3.10",
    entry_points={
        "console_scripts": [
            "econ-agent=src.cli:main",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
)

