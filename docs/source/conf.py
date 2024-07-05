# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys

# The os.path.abspath() function converts a relative path to an absolute path.
# '..' is a relative path that refers to the parent directory of the current directory.
# So, os.path.abspath('..') returns the absolute path of the parent directory of the current working directory.
# The sys.path list in Python holds the directories that the interpreter searches for modules to import.
# insert(0, ...) adds the given path at the beginning of the sys.path list.
# By inserting at index 0, this path is given the highest priority when Python searches for modules to import.

sys.path.insert(0, os.path.abspath('../..'))

project = 'Math'
copyright = '2024, Abdul Nelfrank'
author = 'Abdul Nelfrank'
release = 'v.1.1.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode'
]

templates_path = ['_templates']
exclude_patterns = [
    'build',
    'Thumbs.db',
    '.DS_Store'
]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
