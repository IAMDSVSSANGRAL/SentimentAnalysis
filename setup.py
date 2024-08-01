from setuptools import find_packages,setup
from typing import List

# to automate the process installing requiremnts.txt
def get_requirements()-> List[str]:

    requirements_list = list[str] = []

    return requirements_list



setup(
name = 'sentiment',
version='0.0.1',
author='Havinosh',
author_email = 'support@havinosh.com',
packages = find_packages(),
install_requires = get_requirements(),#['numpy','pandas']

)