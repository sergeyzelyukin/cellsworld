from setuptools import find_packages, setup

setup(
    name="cellsworld",
    version="0.007",
    packages=find_packages("cellsworld"),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "cellsworld=cellsworld.cellsworld:start",
        ]
    },
)
