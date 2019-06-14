# gatlab_tools.accessories

This package provides accessory functions, classes and decorations to be used with various basic data types, packages.

## Installation

Using `pip`:

    pip install -e 'git+https://github.com/gatfieldlab/tools_accessories#egg=gatlab-tools-accessories'
    
From `setup.py` with `setuptools`:

    install_requires = ['gatlab-tools-accessories-VERSION']
    dependency_links = ['http://github.com/gatfieldlab/tools_accessories/tarball/master#egg=gatlab-tools-accessories-VERSION']

Replace `VERSION` with the current version, for example 0.1.0

Modules should be imported using the `gatlab_tools` namespace:

    from gatlab_tools.accessories import align_utils

