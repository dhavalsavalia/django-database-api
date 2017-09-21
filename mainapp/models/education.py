from django.db import models
from mainapp import helpers
from django.utils.translation import ugettext_lazy as _


class Education(models.Model):
    persondata = models.ForeignKey("mainapp.PersonData", related_name='educations')

    institute = models.CharField(max_length=100, verbose_name=_("Institute"))
    discipline = models.CharField(max_length=100, verbose_name=_("Discipline"))
    description = models.TextField(max_length=200 ,blank=True, null=True, verbose_name=_("Description"))
    grades = models.CharField(max_length=4, blank=True, null=True, verbose_name=_("Grades"))

    start_year = models.IntegerField(choices=helpers.YEARS, default=helpers.current_year, verbose_name=_("Start year"))
    start_month = models.IntegerField(choices=helpers.MONTHS, default=helpers.current_month, verbose_name=_("Start month"))
    still = models.BooleanField(default=True, verbose_name=_("Currently studying"))
    end_year = models.IntegerField(choices=helpers.YEARS, null=True, blank=True, verbose_name=_("End year"))
    end_month = models.IntegerField(choices=helpers.MONTHS, null=True, blank=True, verbose_name=_("End month"))

    class Meta:
        app_label = 'mainapp'
        ordering = ('-start_year', )

    def __str__(self):
        return self.institute
