# Generated by Django 2.2.1 on 2019-11-16 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trivia', '0009_auto_20191116_0340'),
    ]

    operations = [
        migrations.AddField(
            model_name='attempt',
            name='total_cards',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]