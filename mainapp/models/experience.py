from django.db import models
from mainapp import helpers
from django.utils.translation import ugettext_lazy as _


EXPERIENCE_TYPES = (
    (None, _('unknown')),
    ('SALAR', _('salaried')),
    ('CHIEF', _('founder/chief')),
    ('FREEL', _('freelance/chief')),
    ('OTHER', _('other')),
)


class Experience(models.Model):
    persondata = models.ForeignKey("mainapp.PersonData", related_name='experiences')

    title = models.CharField(max_length=200, verbose_name=_("title"))
    entreprise = models.CharField(max_length=200, verbose_name=_("entreprise"))
    context = models.TextField(max_length=1000, blank=True, verbose_name=_("context"))
    description = models.TextField(max_length=3000, blank=True, verbose_name=_("description"))
    type = models.CharField(choices=EXPERIENCE_TYPES, max_length=5, null=True, verbose_name=_("type"))
    environment = models.CharField(max_length=400, blank=True, verbose_name=_("environment"))

    start_year = models.IntegerField(choices=helpers.YEARS, default=helpers.current_year, verbose_name=_("start year"))
    start_month = models.IntegerField(choices=helpers.MONTHS, default=helpers.current_month, verbose_name=_("start month"))
    still = models.BooleanField(default=True, verbose_name=_("still in office"))
    end_year = models.IntegerField(choices=helpers.YEARS, null=True, blank=True, verbose_name=_("end year"))
    end_month = models.IntegerField(choices=helpers.MONTHS, null=True, blank=True, verbose_name=_("end month"))

    class Meta:
        app_label = 'mainapp'

    def __str__(self):
        return _('%(title)s at %(entreprise)s') % \
                {'title': self.title, 'entreprise': self.entreprise}
