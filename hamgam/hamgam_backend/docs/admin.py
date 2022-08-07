from django.contrib import admin
from .models import Doc
# Register your models here.
from django import forms
from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class DocAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Doc
        fields = '__all__'

    class Media:
        js = ('ckeditor.js',)
        # do not write '/static/ck

class DocAdmin(admin.ModelAdmin):
    form = DocAdminForm

admin.site.register(Doc, DocAdmin)