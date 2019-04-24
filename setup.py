import sys
from setuptools import setup

if sys.version_info < (3, 5, 3):
    raise RuntimeError("Py-serpost requires Python 3.5.3+")

setup(name='py-serpost',
      version='0.4.0',
      description='Tracking de paquetes de Serpost Perú sin autenticación',
      long_description=open('README.rst').read(),
      url='https://github.com/wesitos/py-serpost',
      author='Pedro Palacios',
      keywords='serpost tracking',
      license='GPL-3.0+',
      packages=['serpost'],
      install_requires=[
          'aiohttp>=3.1.3',
          'pyyaml>=4.2b1',
      ],
      python_requires='>=3.5.3',
      entry_points={
          'console_scripts': [
              'serpost=serpost.cmd:main',
          ],
      },
      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Console',
          'Framework :: AsyncIO',
          'Intended Audience :: End Users/Desktop',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Topic :: Utilities',
      ],
)
