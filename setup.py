from setuptools import setup
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='PythonandDragons',
    version='0.0.4',    
    description='DND functions in python!',
    url='https://github.com/Knights-of-Dev/PythonandDragons',
    author='Pitchfork7',
    author_email='example@example.com',    
    license='MIT',
    packages=['PythonandDragons'],
    install_requires=[],
    long_description=long_description,
    long_description_content_type='text/markdown',

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: Freeware',  
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Programming Language :: Python :: 3.14',
        'Programming Language :: Python :: 3.15'
    ],
)    
