from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
import pytz

ALL_TIME_ZONE_CHOICES = [(tz, tz) for tz in pytz.all_timezones]
COMMON_TIME_ZONE_CHOICES = [(tz, tz) for tz in pytz.common_timezones]


class TimeZoneField(models.CharField):
    """
    Stores pytz.timezone objects in the database.
    """

    max_length = 64
    description = _('Stores pytz.timezone objects in the database.')

    def __init__(self, *args, **kwargs):
        """
        choices: COMMON_TIME_ZONE_CHOICES
        default: settings.TIME_ZONE
        """
        kwargs['choices'] = kwargs.get('choices', COMMON_TIME_ZONE_CHOICES)
        kwargs['default'] = kwargs.get('default', settings.TIME_ZONE)
        return super(TimeZoneField, self).__init__(*args, **kwargs)

    def to_python(self, value):
        """
        Package value up as pytz.timezone object.
        """
        return pytz.timezone(value)

    def get_prep_value(self, value):
        """
        Extract string name for pytz.timezone object.
        """
        return value.zone


class LanguageField(models.CharField):
    """
    Stores language codes in two char ("en") or 5 char ("en_US", "en-us") format.
    """

    max_length = 5
    description = _('Stores language codes in two char ("en") or 5 char ("en_US", "en-us") format.')

    def __init__(self, *args, **kwargs):
        """
        choices: settings.LANGUAGE
        default: settings.LANGUAGE_CODE
        """
        kwargs['choices'] = kwargs.get('choices', settings.LANGUAGES)
        kwargs['default'] = kwargs.get('default', settings.LANGUAGE_CODE)
        return super(LanguageField, self).__init__(*args, **kwargs)