from django.utils import timezone, translation
from django.conf import settings
import pytz


class TimeZoneMixin(object):
    """
    Mix with generic view to add time zone support in templates.
    NOTE: This should be left of the view class.
    """

    time_zone_name = settings.TIME_ZONE

    def render_to_response(self, *args, **kwargs):
        timezone.activate(self.get_time_zone())
        return super(TimeZoneMixin, self).render_to_response(*args, **kwargs)

    def get_time_zone(self):
        return pytz.timezone(self.get_time_zone_name())

    def get_time_zone_name(self):
        return self.time_zone_name

class LanguageMixin(object):
    """
    Mix with generic view to add language support in templates.
    NOTE: This should be left of the view class.
    """

    language = settings.LANGUAGE_CODE

    def render_to_response(self, *args, **kwargs):
        translation.activate(self.get_language())
        return super(LanguageMixin, self).render_to_response(*args, **kwargs)

    def get_language(self):
        return self.language