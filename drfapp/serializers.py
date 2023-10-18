from rest_framework import serializers
from . models import students

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model= students
        # fields=['id','name','marks','dateofbirth','gender']
        fields = '__all__'