

from setuptools import find_packages, setup

setup(
    name="open-cv",
    packages=find_packages(),
    install_requires=["mtcnn","tensorflow","opencv-python"],
    extras_required={"develop": []}
)
