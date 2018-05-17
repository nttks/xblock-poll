"""
Settings for xblock-poll
"""

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': 'intentionally-omitted',
    },
}

INSTALLED_APPS = (
    'django_nose',
    'poll',
    'workbench',
)

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

NOSE_ARGS = [
    '--with-coverage',
    '--cover-html',
    '--cover-package=poll',
    '--cover-erase',
]

STATIC_URL = '/static/'
STATIC_ROOT = ''
SECRET_KEY = 'poll_SECRET_KEY'
