# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import sys
import os
import datetime

sys.path.append(os.path.abspath(''))
sys.path.append(os.path.abspath('../../src/'))

project = 'py2ren'
copyright = '2024-{}, Yoimer Davila'.format(datetime.date.today().year)
author = 'Yoimer Davila'
release = '1.0'
version = release + " Documentation"

html_title = project.capitalize() + " Documentation"
extensions = [
    'sphinx_rtd_theme',
    "sphinx_copybutton",
    'autoapi.extension',
    'sphinx_mdinclude',
    "extensions.short_module",
    "extensions.title_as_you_type",
    "extensions.multi_directive",
    "extensions.renpylexer.extension",
]

rst_prolog = """
.. |br| raw:: html

   <br />
"""

# html_file_suffix = ''

lunrsearch_highlight = True

highlight_language = "python"

pygments_style = 'default'

html_css_files = [
    "css/{}.css".format(name)
    for name in ("fabup", "code-syntax", "font-jb-sans", "index")
]
html_js_files = [
    "js/{}.js".format(name)
    for name in ("fabup", "code-syntax", "index", 'icon-fixer')
]

templates_path = [
    '_templates'
]

locale_dirs = ["locale/"]

exclude_patterns = []

source_suffix = '.rst'

html_theme = 'sphinx_rtd_theme'

html_static_path = ['_static']

html_theme_options = {
    'sticky_navigation': False,
}

master_doc = 'index'

html_show_sourcelink = False

html_permalinks = True


# html_favicon = "img/favicon.ico"
# html_logo = "img/navbar-logo.png"

autodoc_member_order = autoapi_member_order = "groupwise"

autoclass_content = autoapi_python_class_content = "both"

add_module_names = False

autoapi_dirs = ['../../py2ren']

autoapi_options = [
    'members', 'undoc-members',
    'show-inheritance', 'show-module-summary',
    'special-members', 'imported-members',
]

autoapi_generate_api_docs = False

autoapi_file_patterns = ['*.pyi', '*.py']

# short_module
shortmd_modules = ["py2ren", ".config", ".helpers"]

# title_as_you_type
tyasutype_title_mode = 'short'
tyasutype_exclude_titles = True
tyasutype_navigation_mode = 'infinite'
tyasutype_max_results = 8
tyasutype_relative_url = "py2ren/docs/{}".format(release)

