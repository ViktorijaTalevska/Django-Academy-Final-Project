from .models import Courses,Participant,Instructor
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User

class CoursesSeri(ModelSerializer):
    class Meta:
        model=Courses
        fields = ["name","number_of_participants","start_date","number_of_classes","description","price","category","instructor_id"]
        