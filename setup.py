from setuptools import setup

setup(name='py-dag',
      version='2.0.0',
      use_2to3=True,
      description='Directed acyclic graph implementation',
      url='https://github.com/thieman/py-dag',
      author='Travis Thieman',
      author_email='travis.thieman@gmail.com',
      license='MIT',
      packages=['dag'],
      test_suite='nose.collector',
      tests_require=['nose'],
      zip_safe=False)
