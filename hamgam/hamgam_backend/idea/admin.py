from django.contrib import admin
from .models import Idea,Category,Comment, Like


# Register your models here


admin.site.register(Idea)
admin.site.register(Category)
#admin.site.register(SubCategory)
admin.site.register(Comment)
admin.site.register(Like)