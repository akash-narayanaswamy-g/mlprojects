from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path)->List[str]:
    requirements=[]
    with open(file_path) as obj:
        requirements=obj.readlines()
        requirements=[req.replace('\n','') for req in requirements]
        
        if "-e." in requirements:
            requirements.remove("-e.")

        return requirements

setup(
    name='akash',
    version='0.0.1',
    author='akash',
    author_email='akashnarayanaswamy.ng@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
)