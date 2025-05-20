#!/bin/bash
# -*- coding: utf-8 -*-

from __future__ import division, print_function, unicode_literals

from datetime import datetime

from recommonmark.parser import CommonMarkParser

extensions = ['myst_parser', 'sphinx_tabs.tabs', 'sphinx_rtd_size', 'sphinx_rtd_theme']
templates_path = ['templates', '_templates', '.templates']
source_suffix = ['.rst', '.md']
source_parsers = {
            '.md': CommonMarkParser,
        }
master_doc = 'index'
project = u'Energy Monitor'
copyright = str(datetime.now().year)
version = 'latest'
release = 'latest'
exclude_patterns = ['_build']
pygments_style = 'sphinx'
htmlhelp_basename = 'energymonitor'
html_theme = 'sphinx_rtd_theme'
html_theme_options = {'body_max_width': None}
file_insertion_enabled = False
latex_documents = [
  ('index', 'energymonitor.tex', u'Energy Monitor Documentation',
   u'', 'manual'),
]