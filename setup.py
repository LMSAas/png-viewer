#!/usr/bin/env python

from setuptools import setup, find_packages


setup(
    name="underpy",
    version="0.0.0",
    long_description=__doc__,
    packages=find_packages(include=['underpy']),
    include_package_data=True,
    zip_safe=False,
    install_requires=['imageio', 'matplotlib', 'click'],
    entry_points={
        'gui_scripts': [
            'png-view = png_viewer:png_view'
        ],
    })

import imageio
imageio.plugins.freeimage.download()
