# Generated by Django 2.2.1 on 2019-08-19 12:52

from django.db import migrations, models
import utilities.helper


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_auto_20190818_1044'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameSetting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_smart_users', models.SmallIntegerField(default=80)),
                ('min_user_limit', models.SmallIntegerField(default=600)),
            ],
        ),
        migrations.AlterField(
            model_name='slider',
            name='image',
            field=models.ImageField(upload_to=utilities.helper.Helper.slider_image_upload),
        ),
    ]
