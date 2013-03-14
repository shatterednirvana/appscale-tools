import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
  return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
  name = "appscale-tools",
  version = "1.6.8",
  author = "Chris Bunch",
  author_email = "chris@appscale.com"
  description = ("AppScale Command-line Tools"),
  license = "New BSD",
  keywords = "appscale google-app-engine python java go",
  url = "http://github.com/AppScale/appscale/wiki",
  scripts = ['bin/appscale', 'bin/appscale-add-instances',
    'bin/appscale-add-keypair', 'bin/appscale-describe-instances',
    'bin/appscale-gather-logs', 'bin/appscale-remove-app',
    'bin/appscale-reset-pwd', 'bin/appscale-run-instances',
    'bin/appscale-terminate-instances', 'bin/appscale-upload-app'],
  packages = ['appscale', 'appscale.test'],
  long_description = read('README'),
  classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Topic :: Utilities",
    "License :: OSI Approved :: BSD License",
    "Programming Language :: Python :: 2.6",
    "Programming Language :: Python :: 2.7",
  ],
  install_requires = [
    "termcolor",
    "SOAPpy",
    "pyyaml",
    "boto == 2.6",
    "argparse"
  ],
)
