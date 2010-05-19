from setuptools import setup, find_packages
import sys, os

# Note to distro packagers: This application requires Cement API 
# version 0.7-0.8:20100210

setup(name='helloworld',
    version='0.1',
    description='',
    classifiers=[], 
    keywords='',
    author='',
    author_email='',
    url='',
    license='',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "ConfigObj",
        "Genshi",
        "Cement >=0.8.1, <0.9",
        # Uncomment to use shared plugins from The Rosendale Project.
        #"Rosendale",
        ],
    setup_requires=[
        ],
    test_suite='nose.collector',
    entry_points="""
    [console_scripts]
    helloworld = helloworld.core.appmain:main
    """,
    namespace_packages=[
        'helloworld', 
        'helloworld.bootstrap',
        'helloworld.controllers',
        'helloworld.model',
        'helloworld.helpers',
        'helloworld.templates',
        ],
    )