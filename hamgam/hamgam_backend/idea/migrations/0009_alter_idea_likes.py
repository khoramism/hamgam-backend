# Generated by Django 3.2.14 on 2022-07-22 18:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('idea', '0008_auto_20220722_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea',
            name='likes',
            field=models.ForeignKey(blank=True, default=2, on_delete=django.db.models.deletion.CASCADE, related_name='idea_likes', to='idea.like'),
        ),
    ]