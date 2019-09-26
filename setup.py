#!/usr/bin/env python

from setuptools import setup, find_packages


setup(
    name='django-otp-sns',
    version='0.1.1',
    description="A django-otp plugin that delivers tokens via Amazon SNS.",
    long_description=open('README.rst').read(),
    author='Critical Start',
    author_email='pavel.yershov@criticalstart.com, vasu@criticalstart.com',
    url='https://github.com/vnagendra/django-otp-sns',
    license='BSD',
    classifiers=[
        "Development Status :: 1 - Prototype",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Topic :: Security",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Django",
    ],
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    install_requires=[
        'django-otp >= 0.5.0',
        'boto3 >= 1.9.223',
        'botocore >= 1.12.223',
    ],
)
