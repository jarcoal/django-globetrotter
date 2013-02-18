from django.conf.settings import TIME_ZONE
import pytz

ALL_TIME_ZONE_CHOICES = [(tz, tz) for tz in pytz.all_timezones]
COMMON_TIME_ZONE_CHOICES = [(tz, tz) for tz in pytz.common_timezones]


class TimeZoneField(models.CharField):
    """
    Stores pytz tzinfo object in the a CharField
    """

    max_length = 64
    description = 'Stores pytz tzinfo object in the a CharField'

    def __init__(self, *args, **kwargs):
        """
        Set some values for the CharField

        choices: COMMON_TIME_ZONE_CHOICES
        default: settings.TIME_ZONE
        """
        kwargs['choices'] = kwargs.get('choices', COMMON_TIME_ZONE_CHOICES)
        kwargs['default'] = kwargs.get('default', TIME_ZONE)
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