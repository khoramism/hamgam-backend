from django.shortcuts import render
from rest_framework import generics 
from .models import Skill 
from .serializers import SkillListSerializer,SkillCreateSerializer, SkillDetailSerializer, SkillCreateSerializer, SkillUpdateSerializer
# Create your views here.


class ListSkill(generics.ListCreateAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillListSerializer


class DetailSkill(generics.RetrieveAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillDetailSerializer

class CreateSkill(generics.CreateAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillCreateSerializer

class UpdateSkill(generics.UpdateAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillUpdateSerializer


class DeleteSkill(generics.DestroyAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillDetailSerializer
