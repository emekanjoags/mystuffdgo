# Generated by Django 2.2.1 on 2019-11-11 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trivia', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='closed_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
