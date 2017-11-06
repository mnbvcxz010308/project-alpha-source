#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Vipin G S'
SITENAME = 'EssentialDataScience'
SITEURL = 'https://blog.vipings.com'
PATH = 'content'
TIMEZONE = 'Asia/Kolkata'
DEFAULT_LANG = 'en'

#------THEME SPECIFIC---------------------
# Theme
THEME = 'themes/MinimalXY'

# Theme customizations
MINIMALXY_CUSTOM_CSS = 'static/custom.css'
MINIMALXY_FAVICON = 'favicon.ico'
MINIMALXY_START_YEAR = 2017
# MINIMALXY_CURRENT_YEAR = date.today().year

# Author
AUTHOR_INTRO = u'Hello world! I’m John Doe.'
AUTHOR_DESCRIPTION = u'Hello world! I’m John Doe. I like coffee, birds and Python.'
AUTHOR_AVATAR = 'http://www.gravatar.com/avatar/abcdefghijkl?s=240'
AUTHOR_WEB = 'http://mypersonalsite.com'

# Services
GOOGLE_ANALYTICS = 'UA-12345678-9'
DISQUS_SITENAME = 'johndoe'

# Social
SOCIAL = (
    ('facebook', 'http://www.facebook.com/johndoe'),
    ('twitter', 'http://twitter.com/johndoe'),
    ('github', 'https://github.com/johndoe'),
    ('linkedin', 'http://www.linkedin.com/in/johndoe'),
)

# Menu
# MENUITEMS = (
#     ('Categories', '/' + CATEGORIES_SAVE_AS),
#     ('Archive', '/' + ARCHIVES_SAVE_AS),
# )
#---------------THEME SPECIFIC END----------------------------
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# # Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

DEFAULT_PAGINATION = 10
MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = './plugins'
PLUGINS = ['ipynb.markup']
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
