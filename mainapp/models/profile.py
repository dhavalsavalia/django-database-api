from django.db import models
from mainapp import helpers
from django.utils.translation import ugettext_lazy as _


class PersonData(models.Model):
    first_name = models.CharField(max_length=50, verbose_name=_("First Name"))
    last_name = models.CharField(max_length=50, verbose_name=_("Last Name"))
    about = models.TextField(max_length=160, blank=True, null=True, verbose_name=_("About Me"))
    title = models.CharField(max_length=50, verbose_name=_("Title"))
    profile_pic = models.ImageField(upload_to='profile_pic', blank=True, null=True, verbose_name=_("Profile picture"))
    DOB = models.DateTimeField(verbose_name=_("Date of birth"))

    email = models.EmailField(max_length=100, unique=True, verbose_name=_("Email"))
    gender = models.CharField(max_length=1, choices=helpers.GENDER_CHOICES, verbose_name=_("Gender"))
    phone_number = models.CharField(max_length=10, unique=True, verbose_name=_("Phone number"))
    website = models.URLField(max_length=50, blank=True, null=True, verbose_name=_("Website"))
    city = models.CharField(max_length=50, verbose_name=_("City"))
    country = models.CharField(max_length=50, verbose_name=_("Country"))
    state = models.CharField(max_length=50, verbose_name=_("State"))
    address = models.CharField(max_length=200, blank=True, null=True, verbose_name=_("Address"))

    facebook = models.CharField(max_length=50, blank=True, null=True, verbose_name=_("Facebook"))
    google = models.CharField(max_length=100, blank=True, null=True, verbose_name=_("Google+"))
    twitter = models.CharField(max_length=50, blank=True, null=True, verbose_name=_("Twitter"))
    youtube = models.CharField(max_length=50, blank=True, null=True, verbose_name=_("Youtube"))
    github = models.CharField(max_length=50, blank=True, null=True, verbose_name=_("Github"))
    stackoverflow = models.IntegerField(blank=True, null=True, verbose_name=_("Stack Overflow"))
    instagram = models.CharField(max_length=50, blank=True, null=True, verbose_name=_("Instagram"))
    linkedin = models.CharField(max_length=50, blank=True, null=True, verbose_name=_("LinkedIn"))


    class Meta:
        app_label = 'mainapp'
        verbose_name = _('profiledata')

    def __str__(self):
        return "{0} {1} - {2}".format(self.first_name, self.last_name, self.title)

