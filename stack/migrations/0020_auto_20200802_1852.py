# Generated by Django 2.2.1 on 2020-08-02 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stack', '0019_auto_20200801_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bonusbutton',
            name='active',
            field=models.IntegerField(default=0, null=True),
        ),
    ]