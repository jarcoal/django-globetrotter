from django.conf import settings
from django.conf.urls import patterns
from django.core.urlresolvers import LocaleRegexURLResolver
from django.utils.translation import get_language
import re


class NoDefaultPrefixLocaleRegexURLResolver(LocaleRegexURLResolver):
    """
    Source: https://gist.github.com/cauethenorio/4948177
    """
    @property
    def regex(self):
        language_code = get_language()

        if language_code not in self._regex_dict:
            self._regex_dict[language_code] = re.compile('', re.UNICODE) if language_code == settings.LANGUAGE_CODE else re.compile('^%s/' % language_code, re.UNICODE)

        return self._regex_dict[language_code]

def no_default_prefix_i18n_patterns(prefix, *args):
    """
    Functions like Django's i18n_patterns except it doesn't prefix default language URLs.

    Source: https://gist.github.com/cauethenorio/4948177
    """
    pattern_list = patterns(prefix, *args)

    if not settings.USE_I18N:
        return pattern_list

    return [NoDefaultPrefixLocaleRegexURLResolver(pattern_list)]