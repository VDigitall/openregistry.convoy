from setuptools import setup, find_packages

version = '0.1'

requires = [
    'setuptools',
    'gevent',
    'pyyaml',
    'couchdb',
    'couchapp',
    'openprocurement_client'
]

test_requires = [
    'webtest',
    'python-coveralls',
    'nose',
    'mock'
]

extras_requires = {
    'test': requires + test_requires
}

entry_points = {
    'console_scripts': [
        'openregistry_convoy = openregistry.convoy.convoy:main'
    ]
}

setup(name='openregistry.convoy',
      version=version,
      description="openregistry.convoy",
      long_description='openregistry.convoy',
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
          "Programming Language :: Python",
      ],
      keywords='Bot',
      author='Quintagroup, Ltd.',
      author_email='info@quintagroup.com',
      url='https://github.com/openprocurement/openregistry.convoy',
      license='Apache License 2.0',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['openregistry'],
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_requires=test_requires,
      extras_requires=extras_requires,
      entry_points=entry_points,
      )
