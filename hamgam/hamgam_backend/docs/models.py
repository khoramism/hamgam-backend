from django.db import models
from django.urls import reverse
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField
from config.shared import Postable
from skill.models import Skill

class Doc(Postable):

	number = models.PositiveIntegerField(verbose_name='شماره داکیومنت')

	#content = RichTextUploadingField()
	content_persian = RichTextUploadingField() 
	content_english = RichTextUploadingField() 
	books_audiobooks_persian = RichTextUploadingField()
	books_audiobooks_english = RichTextUploadingField() 
	persian_podcasts = RichTextUploadingField()
	english_podcasts = RichTextUploadingField()	

	developed_by = models.URLField(blank=True,null=True)
	
	skill = models.ForeignKey(Skill, on_delete=models.CASCADE)

