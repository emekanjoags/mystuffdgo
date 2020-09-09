# Generated by Django 2.2.1 on 2019-07-31 12:52

from django.db import migrations, models
import utilities.helper


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20190725_1017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(default='uploads/profile/no-img.png', upload_to=utilities.helper.Helper.user_upload_file_name),
        ),
    ]
