from django.db import models
from mainapp import helpers
from django.utils.translation import ugettext_lazy as _


class Training(models.Model):
    persondata = models.ForeignKey("mainapp.PersonData", related_name='trainings')

    school = models.CharField(max_length=150, verbose_name=_("school"))
    degree = models.CharField(max_length=150, verbose_name=_("degree"))
    topic = models.CharField(max_length=150, blank=True, verbose_name=_("topic"))
    result = models.CharField(max_length=150, blank=True, verbose_name=_("result"))
    description = models.TextField(max_length=3000, blank=True, verbose_name=_("description"))

    year = models.IntegerField(choices=helpers.YEARS, verbose_name=_("year"))
    month = models.IntegerField(choices=helpers.MONTHS, verbose_name=_("month"))

    class Meta:
        app_label = 'mainapp'

    def __str__(self):
        return self.degree
