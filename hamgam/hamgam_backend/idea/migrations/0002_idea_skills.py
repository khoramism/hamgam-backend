# Generated by Django 3.1.14 on 2023-03-02 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skill', '0001_initial'),
        ('idea', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='idea',
            name='skills',
            field=models.ManyToManyField(related_name='idea_skills', to='skill.Skill'),
        ),
    ]
