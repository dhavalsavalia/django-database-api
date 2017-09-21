from rest_framework import serializers
from mainapp.models.profile import PersonData
from mainapp.models.education import Education
from mainapp.models.training import Training
from mainapp.models.experience import Experience
from mainapp.models.project import Project, ProjectItem


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education

        fields = [
            'institute',
            'discipline',
            'description',
            'grades',
            'start_year',
            'still',
            'end_year',
        ]


class TrainingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Training

        fields = [
            'school',
            'degree',
            'topic',
            'result',
            'description',
            'year',
            'month'
        ]


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience

        fields = [
            'title',
            'entreprise',
            'context',
            'description',
            'type',
            'environment',
            'start_year',
            'start_month',
            'still',
            'end_year',
            'end_month',
        ]


class ProjectItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectItem

        fields = [
            'project',
            'contribution',
            'start_year',
            'start_month',
            'still',
            'end_year',
            'end_month',
            'weight',
        ]


class ProjectSerializer(serializers.ModelSerializer):
    projectitems = ProjectItemSerializer(many=True)

    class Meta:
        model = Project

        fields = [
            'title',
            'description',
            'url'
            'projectitems',
        ]


class PersonDataSerializer(serializers.ModelSerializer):
    educations = EducationSerializer(many=True)
    trainings = TrainingSerializer(many=True)
    experiences = ExperienceSerializer(many=True)
    projectitems = ProjectItemSerializer(many=True)

    class Meta:
        model = PersonData

        fields = [
                    'first_name',
                    'last_name',
                    'title',
                    'DOB',
                    'email',
                    'phone_number',
                    'gender',
                    'city',
                    'state',
                    'country',
                    'educations',
                    'trainings',
                    'experiences',
                    'projectitems',
                ]
