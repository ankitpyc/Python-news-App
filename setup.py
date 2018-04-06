from setuptools import setup,find_packages
file_path = path.abspath(path.dirname(__file__))
# Get the long description from the README file
with open(path.join(file_path, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='newsApp',

    version='0.1.0',

    description='A python desktopApp for News API (newsapi.org)',
    long_description=long_description,

    url='https://github.com/ankitpyc/NewsApp',

    author='Ankit Mishra',
    author_email='Ankitmishra@gmail.com',

    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',

        'Environment :: Web Environment',
        'Environment :: Console Environment',

        'Operating System :: OS Independent',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    keywords='pynewsapi newsapi newsapi.org news api-client news-feed newsfeeder',

    install_requires=['requests','urllib2'],
)