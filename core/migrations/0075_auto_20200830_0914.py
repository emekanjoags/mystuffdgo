# Generated by Django 2.2.1 on 2020-08-30 08:14

from django.db import migrations, models
import utilities.helper


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0074_auto_20200830_0902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='image',
            field=models.ImageField(upload_to=utilities.helper.Helper.slider_image_upload),
        ),
    ]
