from setuptools import setup

setup(
    name='censure',
    version='0.1',
    description='Detect and filters/replaces obscene/swear words from text/html',
    # long_description='',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Natural Language :: Russian',
        'Natural Language :: English',
        'Topic :: Text Processing :: Filters'
        'Topic :: Text Processing :: Linguistic',
    ],
    keywords='russian english text obscene swears oauth words filtering',
    url='https://github.com/masteroncluster/py-censure',
    author='Cluster-Master',
    author_email='masteroncluster@gmail.com',
    license='GNU',
    packages=['censure'],
    zip_safe=False,

    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
)
