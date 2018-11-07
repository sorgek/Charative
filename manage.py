#!/usr/bin/env python
import os
import sys
import environ

ROOT_DIR = environ.Path(__file__) - 1

if __name__ == "__main__":

    if os.path.isfile('charativeproject/settings/local.py'):
        env = environ.Env(DEBUG=(bool, False), )
        env_file = str(ROOT_DIR.path('.env'))
        print('Loading from manage.py : {}'.format(env_file))
        env.read_env(env_file)
        print('The .env file has been loaded from manage.py. See base.py for more information')

    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    execute_from_command_line(sys.argv)
