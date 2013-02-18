from django.db import models
import fields


class TimeZoneMixin(models.Model):
    """
    Add time zone support to a model.
    """
    time_zone = fields.TimeZoneField()

    class Meta:
        abstract = True

class LanguageMixin(models.Model):
    """
    Add language support to a model.
    """
    language = fields.LanguageField()

    class Meta:
        abstract = True