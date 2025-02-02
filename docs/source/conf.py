# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Modeling API Docs'
copyright = '2023, Radiant Labs'
author = 'Radiant Labs'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['static/']

def setup(app):
    try:
        app.add_css_file("stylesheet.css")
    except:
        app.add_stylesheet("stylesheet.css")

# -- Options for EPUB output
epub_show_urls = 'footnote'
