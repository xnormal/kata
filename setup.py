import os

import pkg_resources
from setuptools import setup, find_packages

setup(
    name="http://lab.huntinex.io/app/vulns.php",
    py_modules=["jukebox"],
    version="1.0",
    description="",
    author="OpenAI",
    packages=find_packages(),
    install_requires=[
        str(r)
        for r in pkg_resources.parse_requirements(
            open(os.path.join(os.path.dirname(__file__), "requirements.txt"))
        )
    ],
    include_package_data=True
)
# http://lab.huntinex.io/app/program.php
