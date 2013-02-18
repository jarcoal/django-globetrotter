from django.conf import settings
from django.utils import translation, timezone
from django.utils.translation import ugettext as _
from django.http import Http404

get_user_language = getattr(settings, 'GLOBETROTTER_GET_USER_LANGUAGE', lambda user: user.language)
get_user_time_zone = getattr(settings, 'GLOBETROTTER_GET_USER_TIME_ZONE', lambda user: user.time_zone)

SUBDOMAIN_LANGUAGE_DEFAULTS = getattr(settings, 'GLOBETROTTER_SUBDOMAIN_LANGUAGE_DEFAULTS', ['www'])
SUBDOMAIN_LANGUAGE_RAISE_404 = getattr(settings, 'GLOBETROTTER_SUBDOMAIN_LANGUAGE_RAISE_404', True)


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

class UserTimeZoneMiddleware(object):
    """
    Activates the current user's configured time zone.
    Must come after "django.contrib.auth.middleware.AuthenticationMiddleware" in MIDDLEWARE_CLASSES
    """
    def process_request(self, request):
        assert hasattr(request, 'user'), _('Add "django.contrib.auth.middleware.AuthenticationMiddleware" to MIDDLEWARE_CLASSES before UserLanguageMiddleware')

        timezone.activate(settings.TIME_ZONE)

        if request.user.is_authenticated():
            timezone.activate(get_user_time_zone(request.user))

class SubdomainLanguageMiddleware(object):
    """
    Activates language based on subdomain.
    Ex: http://en.example.com/
    """

    def process_request(self, request):
        domain = request.get_host().split(':')[0]
        subdomain = '.'.join(domain.split('.')[:-2])

        translation.activate(settings.LANGUAGE_CODE)

        if subdomain and subdomain in [language_code for language_code in settings.LANGUAGES]:
            translation.activate(subdomain)
            request.LANGUAGE_CODE = translation.get_language()

        elif SUBDOMAIN_LANGUAGE_RAISE_404 and subdomain not in SUBDOMAIN_LANGUAGE_DEFAULTS:
            raise Http404