from setuptools import setup, find_packages
import logging
logger = logging.getLogger(__name__)

name = 'feynman_path'
package_name = 'feynman_path'
version = '0.1.0'

try:
    with open('README.md', 'r') as f:
        long_desc = f.read()
except:
    logger.warning('Could not open README.md.  long_description will be set to None.')
    long_desc = None

setup(
    name = package_name,
    packages = find_packages(),
    entry_points = {
        'console_scripts': [
            'feynman_path=feynman_path.command:run_from_command_line',
        ]},
    version = version,
    description = 'Visualization tool for the Feynman Path Integral applied to quantum circuits',
    long_description = long_desc,
    long_description_content_type = 'text/markdown',
    author = 'Casey Duckering',
    #author_email = '',
    url = f'https://github.com/cduck/{name}',
    download_url = f'https://github.com/cduck/{name}/archive/{version}.tar.gz',
    keywords = ['quantum computing', 'feynman path', 'path integral', 'jupyter'],
    classifiers = [
        'License :: OSI Approved :: MIT License',
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Framework :: IPython',
        'Framework :: Jupyter',
    ],
    install_requires = [
        'drawSvg~=1.8',
        'latextools~=0.4',
        'sympy~=1.7',
    ],
)

