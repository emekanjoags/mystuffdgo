# Generated by Django 2.2.1 on 2020-07-22 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0013_manualdeposit_timepaid'),
    ]

    operations = [
        migrations.AddField(
            model_name='manualdeposit',
            name='settled',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
