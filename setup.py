from setuptools import setup, find_packages

VERSION = '0.1.2'

setup(
    name="mkdocs-bootstrap4",
    version=VERSION,
    url='https://github.com/byrnereese/mkdocs-bootstrap4/',
    license='MIT',
    description='Bootstrap4 theme for MkDocs',
    author='Byrne Reese',
    author_email='byrne@majordojo.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['mkdocs>=1.0','mkdocs-git-committers-plugin>=0.1.3'],
    python_requires='>=2.7.9,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*',
    entry_points={
        'mkdocs.themes': [
            'bootstrap4 = mkdocs_bootstrap4',
        ]
    },
    zip_safe=False
)
