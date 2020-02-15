"""Define PyPI package."""

import setuptools

with open("README.md", "r") as readme_file:
    long_description = readme_file.read()

setuptools.setup(
    name='public_suffix_list',
    version='0.0.0',  # version will get replaced by git version tag - do not edit
    author='Peter Linss',
    author_email='pypi@linss.com',
    description='Split domain names into subdomain, registered, and public parts per the Public Suffix List',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/plinss/public_suffix_list/',

    packages=['public_suffix_list'],
    package_data={'public_suffix_list': ['py.typed']},

    install_requires=[
        'typing_extensions',
    ],
    extras_require={
        'dev': ['mypy',
                'flake8', 'flake8-import-order', 'flake8-annotations', 'flake8-type-annotations', 'flake8-docstrings',
                'pep8-naming'],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6'
)
