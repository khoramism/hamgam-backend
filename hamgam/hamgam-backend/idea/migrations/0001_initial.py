# Generated by Django 4.0.5 on 2022-06-22 15:27

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
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='ساخت')),
                ('publish', models.DateTimeField(default=django.utils.timezone.now, verbose_name='انتشار')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='آپدیت')),
                ('active', models.BooleanField(default=True)),
                ('slug', models.SlugField(default='', max_length=100, verbose_name='لینک')),
                ('summary', models.CharField(blank=True, max_length=300, null=True, verbose_name='خلاصه')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'تگ',
                'verbose_name_plural': 'تگ ها ',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='ساخت')),
                ('publish', models.DateTimeField(default=django.utils.timezone.now, verbose_name='انتشار')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='آپدیت')),
                ('active', models.BooleanField(default=True)),
                ('slug', models.SlugField(default='', max_length=100, verbose_name='لینک')),
                ('summary', models.CharField(blank=True, max_length=300, null=True, verbose_name='خلاصه')),
                ('name', models.CharField(max_length=50)),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='idea.category')),
            ],
            options={
                'verbose_name': 'زیرتگ ',
                'verbose_name_plural': 'زیرتگ ها ',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Idea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('pub_date', models.DateTimeField(verbose_name='published date')),
                ('status', models.CharField(choices=[('draft', 'در حال انتظار'), ('published', 'منتشر شده')], default='draft', max_length=60, verbose_name='وضعیت')),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='idea.category')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='idea_creator', to=settings.AUTH_USER_MODEL)),
                ('sub_cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='idea.subcategory')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='ساخت')),
                ('publish', models.DateTimeField(default=django.utils.timezone.now, verbose_name='انتشار')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='آپدیت')),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('commentor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='idea.idea')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
