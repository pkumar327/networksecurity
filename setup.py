from setuptools import find_packages,setup
from typing import List

def get_requirements() -> List[str] :

    req_list:List[str] = []
    try:
        with open('requirements.txt') as file:
            lines = file.readlines()
            for line in lines:
                req = line.strip()
                if req and req!= '-e .':
                    req_list.append(req)
    except FileNotFoundError:
        print("Requirement file not found")

    return req_list

setup(
    name="NetowrkProject",
    version="001",
    author="NJ",
    packages=find_packages(),
    install_requires=get_requirements()
)

print(get_requirements())