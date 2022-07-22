from django.db import models
from django.urls import reverse
import datetime 
from django.utils import timezone
from account.models import Account
#from .idea import Idea



class Like(models.Model):
    liker = models.ForeignKey('account.Account', on_delete=models.CASCADE, blank=False)
    idea = models.ForeignKey('idea.Idea', on_delete=models.CASCADE, blank=False)