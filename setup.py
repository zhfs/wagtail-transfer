#!/usr/bin/env python

from setuptools import find_packages, setup

setup(
    name='wagtail-transfer-loft3di',
    version='0.9.4.10',
    description="Content transfer for Wagtail",
    author='Matthew Westcott',
    author_email='matthew.westcott@torchbox.com',
    url='https://github.com/wagtail/wagtail-transfer',
    packages=find_packages(exclude=('tests',)),
    include_package_data=True,
    install_requires=[
        'wagtail>=5.2'
    ],
    extras_require={
        'docs': [
            'mkdocs>=1.0,<1.1',
            'mkdocs-material>=4.6,<4.7',
        ],
    },
    python_requires=">=3.8",
    license='BSD',
    long_description="An extension for Wagtail allowing content to be transferred between multiple instances of a Wagtail project",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Framework :: Django',
        'Framework :: Django :: 3.2',
        'Framework :: Django :: 4.2',
        'Framework :: Django :: 5.0',
        'Framework :: Wagtail',
        'Framework :: Wagtail :: 5',
        'Framework :: Wagtail :: 6',
    ],
)
