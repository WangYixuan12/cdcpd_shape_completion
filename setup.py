from setuptools import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
    packages=['cdcpd_shape_completion'],
    scripts=['./scripts'],
    package_dir={'': 'src'}
)

setup(**d)