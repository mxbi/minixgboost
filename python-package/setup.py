# pylint: disable=invalid-name, exec-used
"""Setup xgboost package."""
from __future__ import absolute_import
import sys
import os
from setuptools import setup, find_packages
# import subprocess
sys.path.insert(0, '.')

CURRENT_DIR = os.path.dirname(__file__)

# We can not import `xgboost.libpath` in setup.py directly since xgboost/__init__.py
# import `xgboost.core` and finally will import `numpy` and `scipy` which are setup
# `install_requires`. That's why we're using `exec` here.
libpath_py = os.path.join(CURRENT_DIR, 'minixgboost/libpath.py')
libpath = {'__file__': libpath_py}
exec(compile(open(libpath_py, "rb").read(), libpath_py, 'exec'), libpath, libpath)

LIB_PATH = libpath['find_lib_path']()
print("Install libxgboost from: %s" % LIB_PATH)
# Please use setup_pip.py for generating and deploying pip installation
# detailed instruction in setup_pip.py
setup(name='minixgboost',
      version=open(os.path.join(CURRENT_DIR, 'minixgboost/VERSION')).read().strip(),
      # version='0.4a23',
      description="MiniXGBoost Python Package",
      long_description=open(os.path.join(CURRENT_DIR, 'README.rst')).read(),
      install_requires=[
          'numpy',
          'scipy',
      ],
      maintainer='Mikel Bober-Irizar',
      maintainer_email='mikel@mxbi.net',
      zip_safe=False,
      packages=find_packages(),
      # this will use MANIFEST.in during install where we specify additional files,
      # this is the golden line
      include_package_data=True,
      data_files=[('minixgboost', LIB_PATH)],
      url='https://github.com/mxbi/minixgboost')
