from rest_framework import serializers

from .models import *


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class CollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = College
        fields = "__all__"
        depth = 1


class Candidateserializer(serializers.ModelSerializer):
    class Meta:
        model = Applicant
        fields = "__all__"
        # depth = 1
