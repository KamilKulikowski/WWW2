# Generated by Django 4.1.1 on 2022-09-19 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_answer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='answer',
        ),
        migrations.AddField(
            model_name='answer',
            name='is_open',
            field=models.BooleanField(default=False),
        ),
    ]
