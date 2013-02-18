from django.conf import settings
from django.utils import translation
from django.utils.translation import ugettext as _

get_user_language = settings.GLOBETROTTER_GET_USER_LANGUAGE or lambda user: user.language

class UserLanguageMiddleware(object):
	"""
	Activates the current user's configured language.
	Must come after "django.contrib.auth.middleware.AuthenticationMiddleware" in MIDDLEWARE_CLASSES
	"""
	def process_request(self, request):
		assert hasattr(request, 'user'), _('Add "django.contrib.auth.middleware.AuthenticationMiddleware" to MIDDLEWARE_CLASSES before UserLanguageMiddleware')

		translation.activate(settings.LANGUAGE_CODE)

		if request.user.is_authenticated():
			translation.activate(get_user_language(request.user))
			request.LANGUAGE_CODE = translation.get_language()