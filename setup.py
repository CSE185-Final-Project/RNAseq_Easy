from setuptools import setup, find_packages

setup(
    name='my_package',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        '': ['docs/manual.txt', 'scripts/data_vis.R'],
    },
    install_requires=[
        'pandas',
    ],
    entry_points={
        'console_scripts': [
            'scRNAseq_Easy=scripts.scRNAseq_Easy:main',
        ],
    },
)