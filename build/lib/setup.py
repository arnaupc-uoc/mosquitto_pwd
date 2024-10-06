from setuptools import setup

setup(
    name='mosquitto_pwd',
    version='0.1.0',
    description='Mosquitto Password Module as Python package',
    url='https://github.com/arnaupc-uoc',
    author='Arnau Pujol Cabarrocas',
    author_email='arnaupc@uoc.edu',
    license='BSD 2-clause',
    packages=['mosquitto_pwd'],
    install_requires=['passlib==1.7.*'],

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Manufacturing',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Telecommunications Industry',
        'License :: Free for non-commercial use',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Natural Language :: Catalan',
    ],
)
