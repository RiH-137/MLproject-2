from setuptools import setup
from typing import List






#declaring variable for setup function
PROJECT_NAME="housing_preditor"
VERSION="0.0.1"
AUTHOR="Rishi Ranjan"
DESCRIPTION="This is house prediction project."
REQUIREMENT_FILE_NAME="requirements.txt"


#the below function read the requirements.txt file
def get_requirements_list()->List[str]:

    '''
        Description: This function is going to return list of requirements mention in requirements.txt file.

        return This function is going to return a list which contains name
        of libraries mentioned in requirements.txt file
    '''
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines()






setup(name=PROJECT_NAME, version=VERSION, author=AUTHOR, description=DESCRIPTION,
      packages=["housing"], install_requires=get_requirements_list())



if __name__=="__main__":
    print(get_requirements_lis t())