from setuptools import setup, find_packages


setup(
    name='MCColors',
    version='0.1',
    packages=find_packages(),
    description='A Python package for managing Minecraft-style colors in terminal output.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='wRRulos',
    author_email='wrrulos@gmail.com',
    url='https://github.com/wrrulos/MCColors',
    license='MIT License',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Your License',
        'Operating System :: OS Independent',
    ],
    install_requires=[],
)
