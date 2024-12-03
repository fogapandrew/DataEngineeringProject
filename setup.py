from setuptools import setup, find_packages


setup(
    name='src',
    version='0.1',
    description='This is a parkage that uses API and webscraping to get data related to books from different sourcees,',
    author='Njinju ZIlefac Fogap and Njuaka melvin',
    license='MIT',
    packages=find_packages(include=['mypackage']),

    install_requires=['requests' , 'json', 'PIL'] 
) 