# Generated by Django 3.1.14 on 2022-08-30 08:53

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('skill', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='ساخت')),
                ('publish', models.DateTimeField(default=django.utils.timezone.now, verbose_name='انتشار')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='آپدیت')),
                ('active', models.BooleanField(default=True)),
                ('slug', models.SlugField(default='', max_length=100, verbose_name='لینک')),
                ('summary', models.CharField(blank=True, max_length=300, null=True, verbose_name='خلاصه')),
                ('number', models.PositiveIntegerField(verbose_name='شماره داکیومنت')),
                ('content_persian', ckeditor_uploader.fields.RichTextUploadingField()),
                ('content_english', ckeditor_uploader.fields.RichTextUploadingField()),
                ('books_audiobooks_persian', ckeditor_uploader.fields.RichTextUploadingField()),
                ('books_audiobooks_english', ckeditor_uploader.fields.RichTextUploadingField()),
                ('persian_podcasts', ckeditor_uploader.fields.RichTextUploadingField()),
                ('english_podcasts', ckeditor_uploader.fields.RichTextUploadingField()),
                ('developed_by', models.URLField(blank=True, null=True)),
                ('skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='skill.skill')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
