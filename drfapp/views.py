from django.shortcuts import render
from . models import students
from . serializers import StudentSerializer
from rest_framework import generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class StudentList(generics.ListCreateAPIView):
    queryset = students.objects.all()
    serializer_class= StudentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = students.objects.all()
    serializer_class= StudentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]