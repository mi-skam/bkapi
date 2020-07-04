from setuptools import setup, find_packages

setup(name='bkapi',
      version='1.0',
      description='Client for B&K rest api',
      author='Mi-Skam',
      author_email='miskam.codes@mailbox.org',
      url='https://github.com/mi-skam/bkapi',
      packages=find_packages(),
      entry_points={
          "console_scripts": [
              "bkapi = bkapi:main"
          ]
      }
      )
