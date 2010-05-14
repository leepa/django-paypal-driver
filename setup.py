import os
from setuptools import setup

README_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'README')

setup(
    name='django-paypal-driver',
    version='0.1',
    description='Pluggable paypal nvp (Name Value Pair) API implementation for'
                ' django based web applications.',
    long_description=open(README_PATH).read(),
    author='Ozgur Vatansever',
    author_email='ozgurvt@gmail.com',
    url='http://code.google.com/p/django-paypal-driver/',
    packages=['paypal'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved',
        'Operating System :: OS Independent',
        'Framework :: Django',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
    ],
)