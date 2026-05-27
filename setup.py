# Creating ML application as a package and can deplot in pypi

from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path: str) -> List[str]:
    '''
    this fn will return list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace ("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
name='Academic Analysis',
version='2.0.3',
author='Sushil',
author_email='guptasushil5810@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')


)

