"""Loader to retrieve modules from a 'templates' directory within the project
directory"""

import os
import os.path

from django.conf import settings, ENVIRONMENT_VARIABLE as ENV
# ENV is set to 'DJANGO_SETTINGS_MODULE'

from django.template import TemplateDoesNotExist
from django.utils._os import safe_join
from django.utils.importlib import import_module

try:
    if not os.environ[ENV]:
        raise ValueError
        # Catch both KeyErrors and empty values
except (KeyError, ValueError):
    raise ImportError("Settings cannot be imported, because environment "
                      "variable %s is undefined." % ENV)

settings_module = import_module(os.environ[ENV])

def get_template_sources(template_name, template_dirs=None):
    if template_dirs is None:
        template_dirs = []
    for template_dir in template_dirs:
        try:
            template_path = safe_join(template_dir,  template_name)
            yield template_path
        except UnicodeDecodeError:
            # The template dir was a bytestring that wasn't valid UTF-8
            raise
        except ValueError:
            # The joined path was located outside of template_dir
            pass

def load_template_source(template_name, template_dirs=None):
    if not template_dirs:
        project_dir = os.path.dirname(settings_module.__file__)
        project_template_dir = os.path.join(project_dir, 'templates')
        template_dirs = [project_template_dir]
    for filepath in get_template_sources(template_name, template_dirs):
        try:
            return (open(filepath).read().decode(settings.FILE_CHARSET), 
                    filepath)
        except IOError:
            pass
    raise TemplateDoesNotExist, template_name

load_template_source.is_usable = True
