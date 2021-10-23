from django.conf import settings
from django.utils.module_loading import import_string as django_import_string


class AttributeDict(dict):
    """
    Access to dictionary attributes
    """

    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__


def get_django_settings(settings_name='DRF_REGISTRATION'):
    """
    Get settings from django settings

    Args:
        settings_name (string): The name of object to get settings
    """

    return getattr(settings, settings_name, {})


def generate_settings(user_settings, default_settings):
    """
    Generate settings from user configuration or get default values

    Args:
        user_settings (dict): user settings
        default_settings (list, optional): The list of settings properties. Defaults to [].
    """
    result = {}

    for prop in default_settings:
        result[prop] = user_settings.get(prop, default_settings[prop])

    return AttributeDict(result)


def import_string(dotted_path):
    """
    Import a dotted module path and return the attribute/class designated
    by the last name in the path. Raise ImportError if the import failed.

    Args:
        dotted_path (string): The dotted module path
    """

    return django_import_string(dotted_path)


def import_string_list(dotted_paths):
    """
    Import list of module paths

    Args:
        dotted_paths (list): The list of dotted paths to import

    Returns:
        [list]: The list of attributes/classes
    """

    return [import_string(dotted_path) for dotted_path in dotted_paths]
