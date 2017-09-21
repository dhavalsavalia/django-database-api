from django.contrib import admin
from mainapp.models.training import Training
from mainapp.models.project import Project, ProjectItem
from mainapp.models.experience import Experience
from mainapp.models.education import Education
from mainapp.models.profile import PersonData
# Register your models here.

admin.site.register(PersonData)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Project)
admin.site.register(ProjectItem)
admin.site.register(Training)
