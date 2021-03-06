#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'sam zuckerman'
SITENAME = 'programming notes'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

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

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10



THEME = "pelican-elegant-1.3"

DISQUS_SITENAME = 'szuckerman-github-io-1'


LANDING_PAGE_ABOUT = {'title': 'I am full stack developer focusing on data-driven applications',
                      'details': '<p>My name is Sam Zuckerman. I may be reached at <a href="https://github.com/szuckerman" '
                      'target="_blank">Github</a>, <a href="https://twitter.com/samzuckerman" target="_blank">Twitter'
                      '</a>, or <a href="https://www.linkedin.com/in/sampzuckerman/" target="_blank">LinkedIn</a></p>'
                      '<p>I work as a full stack developer analyst using various database and web technologies to '
                      'make data analysis more efficient. I work with the entire pipeline, from data engineering and '
                      'database design to front end UX.</p>'}

PROJECTS = [{
    'name': 'Bookscouter Linear Optimizer',
    'url': 'https://github.com/szuckerman/Bookscouter_LP',
    'description':
    'A program which scrapes bookscouter.com for given ISBN numbers and determines to which stores they should be sent'
    'to maximize profit.'},
    {'name': 'PyJanitor',
    'url': 'https://github.com/ericmjl/pyjanitor',
    'description': '(Contributor) A Python implementation of the R package <a href="https://github.com/sfirke/janitor" target="_blank"'
                   '>janitor</a>, and more. It includes tools for examining and cleaning dirty data.'}]


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
GOOGLE_ANALYTICS = "UA-128575468-1"

ARTICLE_EXCLUDES = [
    'inprogress',
    'python_scripts'
]

STATIC_PATHS = ['images']