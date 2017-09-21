from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import now

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
)

YEARS = [(i, i) for i in range(1900, 2030)][::-1]
MONTHS = (
    (1, _('january')),
    (2, _('febuary')),
    (3, _('march')),
    (4, _('april')),
    (5, _('may')),
    (6, _('june')),
    (7, _('july')),
    (8, _('august')),
    (9, _('september')),
    (10, _('october')),
    (11, _('november')),
    (12, _('december')),
)

DAYS = [(i, i) for i in range(1, 32)][::-1]

WEIGHTS = (
    (0, _('Minor')),
    (1, _('Medium')),
    (2, _('Major')),
)


EDUCATION_LEVELS = (
    (None, _('unknown')),
    ('D', _('degree')),
    ('J', _('junior college')),
    ('S', _('school')),
)


def current_year():
    return now().year


def current_month():
    return now().month
