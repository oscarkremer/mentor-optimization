from setuptools import find_packages, setup


with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name='src',
    packages=find_packages(),
    version='0.2.0',
    description='Pipeline to generate trajectories for robot mentor using artificial intelligence algorithms',
    author='Oscar Schmitt Kremer',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/oscarkremer/mentor-optimization",
)