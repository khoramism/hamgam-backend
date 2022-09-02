from django.shortcuts import render
from rest_framework import generics 
from .models import Skill 
from .serializers import SkillListSerializer,SkillCreateSerializer, SkillDetailSerializer, SkillCreateSerializer, SkillUpdateSerializer
from django.http import HttpResponse
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



from django.core.mail import send_mail
from django.conf import settings 
'''def mail_ko(request):
	pass
	# send_mail(
	#'Th’s your subject',
	#'yomessage body',
	# 'alireza@ham-ghadam.ir',
	# ['momom58856@zfobo.com', 'khoramism@gmail.com'],
	# fail_silently=True,)
	#return HttpResponse('<h1>HelloKIR </h1>')
'''
from django.core.mail import EmailMessage
from django.http import HttpResponse
import traceback

def mail_kon(request):
	try:
		emailto = ['khoramism@gmail.com', 'alirezakhoramimn@gmail.com']
		html_content = "Comment tu vas?"
		email = EmailMessage("my subject", html_content, "alireza@ham-ghadam.ir", emailto)
		email.content_subtype = "html"
		fd = open('manage.py', 'r')
		email.attach('manage.py', fd.read(), 'text/plain')	
		res = email.send()
		return HttpResponse('%s'%res)
	except:
		return HttpResponse(traceback.format_exc())
