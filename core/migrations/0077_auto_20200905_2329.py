# Generated by Django 2.2.1 on 2020-09-05 22:29

from django.db import migrations, models
import utilities.helper


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0076_auto_20200905_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='image',
            field=models.ImageField(upload_to=utilities.helper.Helper.slider_image_upload),
        ),
    ]