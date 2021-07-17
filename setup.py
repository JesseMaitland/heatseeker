from setuptools import setup, find_packages

VERSION = '0.0.1'


setup(
    name='heatseeker',
    version=VERSION,
    author='Jesse Maitland',
    discription='A cli tool to generate a file search result index',
    include_package_data=True,
    packages=find_packages(exclude=('tests*', 'venv')),
    entry_points={'console_scripts': ['seeker = heatseeker.__main__:main']},
    python_requires='>=3'
)
