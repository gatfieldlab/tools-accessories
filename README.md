# gatlab-tools-accessories

This package provides accessory functions, classes and decorations to be used with various basic data types, packages.

## Installation

Using `pip`:

    pip install -e 'git+https://github.com/gatfieldlab/tools_accessories#egg=gatlab-tools-accessories'

or using our Python Package Server as an extra index:

    pip install gatlab-tools-accessories --extra-index-url https://gatfieldlab.github.io/python-package-server/
    
From `setup.py` with `setuptools`:

    install_requires = ['gatlab-tools-accessories-VERSION']
    dependency_links = ['https://github.com/gatfieldlab/tools_accessories/tarball/master#egg=gatlab-tools-accessories-VERSION']

Replace `VERSION` with the current version, for example 0.1.0.

To use a specific version from previous releases:

    dependency_links = ['https://github.com/gatfieldlab/tools_accessories/archive/v0.1.0.tar.gz#egg=gatlab-tools-accessories-0.1.0']
    

Support for `dependency_links` and `setuptools` will not be continued and will be removed in the next releases.

## Usage

Modules should be imported using the `gatlab_tools` namespace:

    from gatlab_tools.accessories import align_utils

