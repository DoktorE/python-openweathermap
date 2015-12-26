import os
from setuptools import setup, find_packages

install_requires = open('requirements.txt').read().splitlines()

__version__ = '0.0.1'


def read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except IOError:
        return ''


setup(
    name='python-openweathermap',
    description='API Wrapper for OpenWeatherMap written in Python',
    version=__version__,
    long_description=read('README.rst'),
    license='Nada',
    platforms=['OS Independent'],
    keywords='wrapper, api, wx, weather, openweathermap',
    author='Doktor',
    author_email='',
    url="https://github.com/doktore/python-openweathermap",
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'License :: OSI Approved :: MIT License',
        'Environment :: Console'
    ]
)