try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config={
    'description': 'My Project',
    'author': 'Caceros',
    'url': 'Nah',
    'download_url': 'Nah',
    'author email': 'caceros995@gmail.com',
    'version': '0.1',
    'install_requires': 'nose',
    'packages': 'my_module',
    'scripts': [],
    'name': 'my project'

} 

setup(**config)