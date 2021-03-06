# Generated by Django 2.2.1 on 2020-08-19 12:33

from django.db import migrations, models
import utilities.helper


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0063_auto_20200804_0845'),
    ]

    operations = [
        migrations.CreateModel(
            name='DefaultImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='uploads/default_img')),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(default='uploads/profile/1/1594598724.png', upload_to=utilities.helper.Helper.user_upload_file_name),
        ),
    ]
