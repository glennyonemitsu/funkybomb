from setuptools import setup


setup(
    name='funkybomb',
    version='0.1',
    description='Quick and wild HTML tree growth',
    author='Glenn Yonemitsu',
    license='Apache License 2.0',
    packages=['funkybomb'],
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.6',
    ],

    setup_requires=['pytest-runner'],
    tests_require=['pytest', 'pytest-cov', 'pytest-flake8'],
)
