# Generated by Django 2.2.1 on 2020-07-22 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0012_manualdeposit'),
    ]

    operations = [
        migrations.AddField(
            model_name='manualdeposit',
            name='timePaid',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
