from setuptools import _install_setup_requires, setup, find_packages

with open('requirements.txt') as file:
    content = file.readlines()
    requirements = [x.strip() for x in content]

setup(
    name='diamond_pkg',
    version='0.0.1',
    packages=find_packages(
        where='diamond',
        include=['*pkg*'],
    ),
    scripts=['scripts/run_diamond'],
    requirements=requirements
)