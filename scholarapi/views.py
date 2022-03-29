from django.shortcuts import render
# Create your views here.
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import *
from .serializers import *


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def retrieve(self, request, *args, **kwargs):
        params = kwargs
        course = params['pk']
        college = Course.objects.get(pk=course)
        serializer = self.serializer_class(college)
        return Response(serializer.data)


class CollegeViewSet(viewsets.ModelViewSet):
    serializer_class = CollegeSerializer

    def get_queryset(self):
        queryset = College.objects.all().order_by('name')
        return queryset

    def retrieve(self, request, *args, **kwargs):
        params = kwargs
        pk = params['pk']
        college = College.objects.get(pk=pk)
        serializer = self.serializer_class(college)
        return Response(serializer.data)


class CandidateViewSet(viewsets.ModelViewSet):
    queryset = Applicant.objects.all()
    serializer_class = Candidateserializer


@api_view(['GET', 'POST', 'HEAD'])
def searchViewSet(request, keyword):
    college_serializer_class = CollegeSerializer
    course_serializer_class = CourseSerializer
    college = College.objects.filter(
        courses__name__icontains=keyword).order_by('name')
    college_serializer = college_serializer_class(college, many=True)
    course = Course.objects.filter(name__icontains=keyword)
    course_serializer = course_serializer_class(
        course, many=True).order_by('name')
    res = {'colleges': college_serializer.data,
           'courses': course_serializer.data}
    return Response(res, headers={"Access-Control-Allow-Origin": "*"})


@api_view(['GET', 'POST', 'HEAD'])
def getCollegewithCourse(request, pk):
    college_serializer_class = CollegeSerializer
    college = College.objects.filter(courses__id=pk).order_by('name')
    college_serializer = college_serializer_class(college, many=True)
    return Response(college_serializer.data, headers={"Access-Control-Allow-Origin": "*"})
