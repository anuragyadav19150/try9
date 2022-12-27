from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from projects.models import Projects,Info,About
from collections import OrderedDict
# Create your views here.

class projects(APIView):
    def get(self,request):
        # print("check 1")

        projectss=Projects.objects.all()
        projectInfo={}

        for x in projectss:
            projectInfo[x.priority]={"firstLine":x.firstLine,"description":x.description,"github":x.github,"image":x.images}

        print(projectInfo)
        projectInfo = OrderedDict(sorted(projectInfo.items()))
        
        infos=Info.objects.all()
        skills={}

        for x in infos:
            skills[x.priority]=x.skill

        print(skills)
        skills = OrderedDict(sorted(skills.items()))

        abouts=About.objects.all()
        firstLine=""
        description=""

        for x in abouts:
            if x.priority==1:
                firstLine=x.firstLine
                description=x.description
                break
        print("sending")
        return Response({
            
            'projectInfo':projectInfo,
            'skills':skills,
            'firstLine':firstLine,
            'description':description,
            
        })
      

   
