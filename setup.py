from setuptools import setup,find_packages
from typing import List






#declaring variable for setup function
PROJECT_NAME="housing_preditor"
VERSION="0.0.3"
AUTHOR="Rishi Ranjan"
DESCRIPTION="This is house prediction project."
REQUIREMENT_FILE_NAME="requirements.txt"
HYPHEN_E_DOT = "-e ."

#the below function read the requirements.txt file
def get_requirements_list()->List[str]:

    '''
        Description: This function is going to return list of requirements mention in requirements.txt file.
            eg., ["numpy"],["pandas"]
        
        return This function is going to return a list which contains name
        of libraries mentioned in requirements.txt file
    '''
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines()
        requirement_list = [requirement_name.replace("\n", "") for requirement_name in requirement_list]
        if HYPHEN_E_DOT in requirement_list:
            requirement_list.remove(HYPHEN_E_DOT)
        return requirement_list






setup(name=PROJECT_NAME, version=VERSION, author=AUTHOR, description=DESCRIPTION,
      packages=find_packages(), #["housing"]
      install_requires=get_requirements_list())



if __name__=="__main__":
    print(get_requirements_list())