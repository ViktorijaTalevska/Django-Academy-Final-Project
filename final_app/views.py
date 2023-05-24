from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Courses,Participant,Enrolment,Instructor
from .serializers import CoursesSeri
import random
import string


class CoursesAPI (APIView):
    def get (self, request):
     all_courses=Courses.objects.filter(user=request.user.id)
     cor_serialized=CoursesSeri(all_courses,many=True)
     return Response(cor_serialized.data)
    def post (self, request):
        pwd_serialized=CoursesSeri(data=request.data)
        if pwd_serialized.is_valid():
            pwd_serialized.save ()
            return Response(pwd_serialized.data)
        else:
            return Response(pwd_serialized.errors)
        
    def patch(self, request):
        pwd_id=request.data.get ("id_number", None) #za da smenime neshto,barame po neshto unikatno vo sluchajot id brojot, ne po pass oti mozhi ist pass za pokje raboti da ima korisnikot
        update=Courses.objects.get(id_number=pwd_id)
        pwd_serialized= CoursesSeri (update, data=request.data, partial=True)
        if pwd_serialized.is_valid ():
            pwd_serialized.save()
            return Response(pwd_serialized.data)
        else:
            return Response(pwd_serialized.errors)
        
    def delete (self, request):
        pwd_id=request.data.get ("id_number", None)
        try:
            id= Courses.objects.get(id_number=pwd_id) #koga brishime, brishime cela redica zato vo edna promenliva zachuvuvame
            id.delete()
        except Courses.DoesNotExist:
            return Response({"info":"Greshka"})
        return Response({"info":"Passwordot e izbrisana"})
