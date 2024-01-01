from setuptools import setup, find_packages

with open("README.md", encoding="utf-8") as f:
    README = f.read()

setup(
    name="PerplexityIPYNB",
    version="1.01",
    description="Perplexity AI in iPython Notebooks",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/vladimirkucin634/PerplexityIPYNB",
    author="vladimirkucin634",
    author_email="vladimirkucin634@mail.ru",
    license="MIT",
    keywords=[
        "artificial-intelligence",
        "perplexityai",
        "perplexity",
        "python",
        "api",
        "ai",
    ],
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
    packages=find_packages(),
    install_requires=[
        "requests",
        "websocket-client",
    ],
    project_urls={
        "Source": "https://github.com/vladimirkucin634/PerplexityIPYNB",
    },
)
