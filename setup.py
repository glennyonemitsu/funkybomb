from setuptools import setup


setup(
    name='Funky Bomb',
    version='0.1',
    description='Quick and nervous html templating',
    author='Glenn Yonemitsu',
    license='Apache License 2.0',
    packages=['funkybomb'],
    zip_safe=False,

    setup_requires=['pytest-runner'],
    tests_require=['pytest', 'pytest-cov', 'pytest-flake8'],
)
