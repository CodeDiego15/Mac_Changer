from setuptools import setup, find_packages

setup(
    name='redeye',
    version='0.1',
    packages=find_packages(),
    python_requires='>=3',
    entry_points={
        'console_scripts': [
            'mac_changer = mac_changer.main:main'
        ]
    },
    install_requires=[
        'colorama',
        'argparse',
        # Agrega aquí otras dependencias
    ]
    
)

