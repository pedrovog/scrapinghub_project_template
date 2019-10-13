# Automatically created by: shub deploy

from setuptools import setup, find_packages

setup(
    name='{{cookiecutter.project_slug}}',
    version='0.1.0',
    packages=find_packages(),
    entry_points={
        'scrapy': [
            'settings = {{cookiecutter.project_module}}.settings',
        ],
    },
    package_data={
        '{{cookiecutter.project_slug}}': [
            '{{cookiecutter.project_slug}}/spiders/resources/*.json',
            '{{cookiecutter.project_slug}}/spiders/resources/*.csv'
        ]
    },
    zip_safe=False,
    include_package_data=True
)
