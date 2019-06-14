from setuptools import setup

setup(
    name='gatlab-tools-accessories',
    version='0.1.0',
    description='Accessory functions, classes and decorations to be '
                'used with various basic data types, packages',
#   url='NA',
    author='Bulak Arpat',
    author_email='bulak.arpat@gmail.com',
    license='GPLv3',
    packages=['gatlab_tools.accessories'],
    install_requires=["colour"],
    zip_safe=False
)
