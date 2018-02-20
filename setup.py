import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-ismobile',
    version='1.0',
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',
    description='A basic "is_mobile" middleware Django app.',
    long_description=README,
    url='https://github.com/cansarigol/django-ismobile',
    author='cansargl',
    author_email='ertugrulsarigol@gmail.com',
    keywords='django,ismobile',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=[
        'django>=1.8',
    ],
)