try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Mini visual novel game.',
    'author': 'Trung',
    'url': 'Not yet.',
    'download_url': 'Not yet.',
    'author_email': 'Not tell you.',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex47'],
    'scripts': [],
    'name': 'ex47'
}

setup(**config)
