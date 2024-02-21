import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name="",
    version='0.1',
    packages=[""],
    author="",
    author_email="",
    maintainer="",
    maintainer_email="",
    download_url='',
    install_requires=[
    ],
    scripts=[
    ],
    include_package_data=True,
    license='Simplified BSD License',
    description="",
    zip_safe=False,
    long_description=README,
    long_description_content_type='text/markdown',
    python_requires='>=3.7',

    #https://pypi.org/classifiers/
    classifiers=[
    ],
)
  
