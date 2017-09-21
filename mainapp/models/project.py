from django.db import models
from mainapp import helpers
from django.utils.translation import ugettext_lazy as _


class Project(models.Model):
    title = models.CharField(max_length=200, unique=True, verbose_name=_("title"))
    description = models.TextField(max_length=3000, blank=True, verbose_name=_("description"))
    url = models.URLField(max_length=300, blank=True, verbose_name=_("URL"))

    class Meta:
        app_label = 'mainapp'

    def __str__(self):
        return self.title


class ProjectItem(models.Model):
    persondata = models.ForeignKey("mainapp.PersonData", related_name='projectitems')
    project = models.ForeignKey("mainapp.Project", related_name='items')
    contribution = models.TextField(max_length=3000, blank=True, verbose_name=_("contribution"))

    start_year = models.IntegerField(choices=helpers.YEARS, default=helpers.current_year, verbose_name=_("start year"))
    start_month = models.IntegerField(choices=helpers.MONTHS, default=helpers.current_month, verbose_name=_("start month"))
    still = models.BooleanField(default=True, verbose_name=_("still contributor"))
    end_year = models.IntegerField(choices=helpers.YEARS, null=True, blank=True, verbose_name=_("end year"))
    end_month = models.IntegerField(choices=helpers.MONTHS, null=True, blank=True, verbose_name=_("end month"))

    weight = models.IntegerField(choices=helpers.WEIGHTS, default=1, verbose_name=_("weight"))

    class Meta:
        app_label = 'mainapp'
        unique_together = ('persondata', 'project')

    def __str__(self):
        return self.project.title
