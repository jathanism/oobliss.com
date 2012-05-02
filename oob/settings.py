# -*- coding: utf-8 -*-
import os

gettext = lambda s: s

PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
    ('Jathan', 'jathan+oobliss@gmail.com'),
)

MANAGERS = ADMINS

LANGUAGES = [('en', 'en')]
DEFAULT_LANGUAGE = 0

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_DIR, 'db/mycms.db'),
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Los_Angeles'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(PROJECT_DIR, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/admin/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '0r6%7gip5tmez*vygfv+u14h@4lbt^8e2^26o#5_f_#b7%cm)u'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.media.PlaceholderMediaMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth', # Adds 'user', 'perms'
    'django.core.context_processors.debug',   # Adds 'debug', 'sql_queries'
    'django.core.context_processors.i18n',    # Adds 'LANGUAGES'
    'django.core.context_processors.request', # Adds 'request'
    'django.core.context_processors.media',   # Adds 'MEDIA_URL'
    'django.core.context_processors.static',  # Adds 'STATIC_URL'
    'cms.context_processors.media',
)

CMS_TEMPLATES = (
    ('example.html', 'Example Template'),
    ('template_1.html', 'Template One'),
    ('template_2.html', 'Template Two'),
    ('music.html', 'Music Template'),
)

#CMS_USE_TINYMCE = False

ROOT_URLCONF = 'oob.urls'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIR, 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'cms',
    'menus',
    'mptt',
    'appmedia',
    'publisher',
    'south',
    # Plugins
    # http://docs.django-cms.org/en/2.1.3/getting_started/plugin_reference.html
    'cms.plugins.file',
    'cms.plugins.googlemap',
    'cms.plugins.inherit',
    'cms.plugins.picture',
    'cms.plugins.link',
    'cms.plugins.snippet',
    'cms.plugins.teaser',
    'cms.plugins.text',
)

#=====================
# Advanced Settings
#=====================
# If set to False, frontend editing is not available for models using
# cms.models.fields.PlaceholderField.
# Default: True
PLACEHOLDER_FRONTEND_EDITING = True

# If this is enabled, pages have the additional template option to inherit their
# template from the nearest ancestor. New pages default to this setting if the
# new page is not a root page.
# Enables the inheritance of templates from parent pages.
# Default: True
CMS_TEMPLATE_INHERITANCE = True

# This adds a new “menu title” field beside the title field.
# With this field you can overwrite the title that is displayed in the menu.
# To access the menu title in the template, use:
# {{ page.get_menu_title }}
# Default: False
CMS_MENU_TITLE_OVERWRITE = False

# This adds a new “redirect” field to the “advanced settings” tab of the page
# You can set a url here, which a visitor will be redirected to when the page is
# accessed.
# Note: Don’t use this too much. django.contrib.redirect is much more flexible,
# handy, and is designed exactly for this purpose.
# Default: False
CMS_REDIRECTS = False

# If this is enabled the slugs are not nested in the urls.
# So a page with a “world” slug will have a “/world” url, even it is a child of
# the “hello” page. If disabled the page would have the url: “/hello/world/”
# Default: False
CMS_FLAT_URLS = False

# This adds a new field “url overwrite” to the “advanced settings” tab of your
# page. With this field you can overwrite the whole relative url of the page.
# Default: True
CMS_URL_OVERWRITE = True

# This adds a new “softroot” field to the “advanced settings” tab of the page. If
# a page is marked as softroot the menu will only display items until it finds
# the softroot.
# If you have a huge site you can easily partition the menu with this.
# Default: False
CMS_SOFTROOT = False

# If set to true, gives you a new “moderation” column in the tree view.
# You can select to moderate pages or whole trees. If a page is under moderation
# you will receive an email if somebody changes a page and you will be asked to
# approve the changes. Only after you approved the changes will they be updated
# on the “live” site. If you make changes to a page you moderate yourself, you
# will need to approve it anyway. This allows you to change a lot of pages for a
# new version of the site, for example, and go live with all the changes at the
# same time.
# Default: False
CMS_MODERATOR = False

# This adds 2 new date-time fields in the advanced-settings tab of the page. With
# this option you can limit the time a page is published.
# Default for both: False
CMS_SHOW_START_DATE = True
CMS_SHOW_END_DATE = True

# This adds a new “SEO Fields” fieldset to the page admin. You can set the Page
# Title, Meta Keywords and Meta Description in there.
# To access these fields in the template use:

# {% load cms_tags %}
# <head>
#   <title>{% page_attribute page_title %}</title>
#   <meta name="description" content="{% page_attribute meta_description %}">
#   <meta name="keywords" content="{% page_attribute meta_keywords %}">
#   ...
#   ...
# </head>
# Default: False
CMS_SEO_FIELDS = True 

# Cache expiration (in seconds) for show_placeholder and page_url template
# tags.
# Default: 60
CMS_CONTENT_CACHE_DURATION = 60

# Cache expiration (in seconds) for the menu tree.
# Default: 3600
MENU_CACHE_DURATION = 3600

# The CMS will prepend the value associated with this key to every cache access
# (set and get). This is useful when you have several Django-CMS installations,
# and you don’t want them to share cache objects.
# Default: None
CMS_CACHE_PREFIX = None
