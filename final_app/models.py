from django.db import models
from django.contrib.auth.models import User

class Courses(models.Model):
 name=models.CharField(max_length=100)
 number_of_participants=models.IntegerField()
 start_date=models.DateField()
 number_of_classes=models.IntegerField()
 description=models.TextField()
 price=models.IntegerField()
 category=models.CharField(max_length=50)
 instructor_id= models.ForeignKey(User, on_delete=models.CASCADE)

class Instructor(models.Model):
  name=models.CharField(max_length=50)
  email=models.CharField(max_length=100)
  phone_number=models.CharField(max_length=50)
  city=models.CharField(max_length=50)
  age=models.IntegerField()
  linkedin_link=models.URLField()
  github_link=models.URLField()


class Participant(models.Model):
  name=models.CharField(max_length=50)
  email=models.CharField(max_length=100)
  phone_number=models.CharField(max_length=50)
  city=models.CharField(max_length=50)
  age=models.IntegerField()
  linkedin_link=models.URLField()
  github_link=models.URLField()
    

class Enrolment(models.Model):
    courseid= models.ForeignKey(Courses, on_delete=models.CASCADE)
    participantid= models.ForeignKey(Participant, on_delete=models.CASCADE)
