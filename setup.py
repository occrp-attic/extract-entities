from setuptools import setup, find_packages


setup(
    name='entityextractor',
    version='1.1.0',
    license='MIT',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    install_requires=[
        'servicelayer == 0.1.4',
    ],
    zip_safe=False
)
