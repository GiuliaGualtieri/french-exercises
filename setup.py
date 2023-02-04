from setuptools import setup

setup(
    name='french_exercises',
    version='0.0.1',
    packages=find_packages(),
    description='Python repository to do practice in french',
    license='MIT',
    install_requires=[
        'torch',
        'transformers',
        'pandas',
        'numpy',
        'random',
    ],
)