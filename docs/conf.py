# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

# Get configuration information from setup.cfg
from configparser import ConfigParser
conf = ConfigParser()
conf.read([os.path.join(os.path.dirname(__file__), '..', 'setup.cfg')])
setup_cfg = dict(conf.items('metadata'))

project = setup_cfg['name']
copyright = '2021, Nicolas Tessore'
author = setup_cfg['author']

# The full version, including alpha/beta/rc tags
release = setup_cfg['version']


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'numpydoc',
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
]

# Add any paths that contain templates here, relative to this directory.
#templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'classic'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
#html_static_path = ['_static']


# -- Options for autodoc -----------------------------------------------------

# Boolean indicating whether to scan all found documents for autosummary
# directives, and to generate stub pages for each. It is disabled by default.
autosummary_generate = True


# -- Intersphinx -------------------------------------------------------------
intersphinx_mapping = {
    'numpy': ('https://numpy.org/doc/stable/', None),
    'scipy': ('https://docs.scipy.org/doc/scipy/reference/', None),
    'healpy': ('https://healpy.readthedocs.io/en/latest/', None),
}
