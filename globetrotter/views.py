from django.utils import timezone
import pytz


class TimeZoneMixin(object):
	"""
	Mix with generic view to add time zone support in templates.
	NOTE: This should be left of the view class.
	"""

	time_zone_name = 'UTC'

	def render_to_response(self, *args, **kwargs):
		timezone.activate(self.get_time_zone())
		return super(TimeZoneMixin, self).render_to_response(*args, **kwargs)

	def get_time_zone(self):
		return pytz.timezone(self.get_time_zone_name())

	def get_time_zone_name(self):
		return self.time_zone_name