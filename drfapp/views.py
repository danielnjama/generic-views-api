from django.shortcuts import render
from . models import students
from . serializers import StudentSerializer
from rest_framework import generics
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.views import APIView
# from django.http import Http404

# Create your views here.
class StudentList(generics.ListCreateAPIView):
    queryset = students.objects.all()
    serializer_class= StudentSerializer

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = students.objects.all()
    serializer_class= StudentSerializer