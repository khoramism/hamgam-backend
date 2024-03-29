# Generated by Django 3.1.14 on 2023-03-02 14:36

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='ساخت')),
                ('publish', models.DateTimeField(default=django.utils.timezone.now, verbose_name='انتشار')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='آپدیت')),
                ('active', models.BooleanField(default=True)),
                ('slug', models.SlugField(default='', max_length=100, verbose_name='لینک')),
                ('summary', models.CharField(blank=True, max_length=300, null=True, verbose_name='خلاصه')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'verbose_name': 'تگ',
                'verbose_name_plural': 'تگ ها ',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='ساخت')),
                ('publish', models.DateTimeField(default=django.utils.timezone.now, verbose_name='انتشار')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='آپدیت')),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('status', models.BooleanField(default=False)),
                ('commentor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Idea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('pub_date', models.DateTimeField(verbose_name='published date')),
                ('status', models.CharField(choices=[('draft', 'در حال انتظار'), ('published', 'منتشر شده')], default='draft', max_length=60, verbose_name='وضعیت')),
                ('cat', models.ManyToManyField(related_name='idea_cats', to='idea.Category')),
                ('comments', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='idea_comments', to='idea.comment')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='idea_creator', to=settings.AUTH_USER_MODEL)),
                ('likes', models.ManyToManyField(blank=True, related_name='idea_likes', to=settings.AUTH_USER_MODEL)),
                ('users', models.ManyToManyField(blank=True, related_name='idea_users', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'ایده',
                'verbose_name_plural': 'ایده ها ',
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='idea.idea')),
                ('liker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='idea',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commments_idea', to='idea.idea'),
        ),
    ]
