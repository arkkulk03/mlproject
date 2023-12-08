from setuptools import find_packages,setup

from typing import List

HYPEN_E_DOT='-e.'
def get_requirements(fule_path:str)->list[str]:


requirements=[]
with open(file_path) as file_obj:
    requirements=file_obj.readlines()
    requirements=[req.replace ("\n","")for req in requirements]

    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)
return requirements   

setup(
name='mlproject,
version='o.o.1',
author='Aditya'
author='aditya.kulkarni200@gmail.com'
packages=find_packages()
install_requires= get_requirements('requiremants.txt')


)