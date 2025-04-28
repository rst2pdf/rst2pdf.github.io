import sys
from pathlib import Path

sys.path.append(str(Path('_ext').resolve()))

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'rst2pdf'
copyright = '2024, rst2pdf project'
author = 'rst2pdf project'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
   "sphinx_copybutton",
   "sphinx_external_toc",
   "rst2pdf.pdfbuilder",
   "noop" # used to ignore rst2pdf-specific directives to make the HTML manual
]

external_toc_path = "_toc.yaml" # "toc" for Table of Contents, this is the navigation
templates_path = ['_templates']
exclude_patterns = ['examples/*']


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_logo = 'assets/rst2pdf-logo.png'
html_favicon = 'assets/favicon.ico'

# -- Options for PDF output --------------------------------------------------

pdf_documents = [('manual', u'rst2pdf', u'rst2pdf documentation', u'rst2pdf project'),]
