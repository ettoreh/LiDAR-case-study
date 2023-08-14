from setuptools import find_packages, setup

setup(
    name="wire-detect",
    packages=find_packages(include=["wire_detect"]),
    version="0.1.0",
    description="Library made to detect wire from LiDAR point cloud dataset",
    author="Me",
    license="MIT"
)
