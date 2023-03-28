from setuptools import find_packages, setup
from typing import List

HYPen_e_dot = '-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirement
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        
        if HYPen_e_dot in requirements:
            requirements.remove(HYPen_e_dot)
    return requirements
        
setup(
    name = 'mlopsproject',
    version = '0.0.1',
    author = 'Jingo',
    author_email = 'jingoasongp@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirement.txt')
)

