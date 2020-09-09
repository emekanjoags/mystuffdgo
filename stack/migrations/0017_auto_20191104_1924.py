# Generated by Django 2.2.1 on 2019-11-04 18:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('stack', '0016_slip_jackpot_check'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activegame',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=40000.0, max_digits=17),
        ),
        migrations.AlterField(
            model_name='activegame',
            name='amount_available',
            field=models.DecimalField(decimal_places=2, default=40000.0, max_digits=17),
        ),
        migrations.AlterField(
            model_name='activegame',
            name='schedule_date',
            field=models.DateField(blank=True, db_index=True, null=True),
        ),
        migrations.AlterField(
            model_name='activegame',
            name='space',
            field=models.IntegerField(default=20),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_name',
            field=models.CharField(db_index=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='match',
            name='clubs_history',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='raffleplayer',
            name='raffle_hash',
            field=models.CharField(db_index=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='slip',
            name='game_fate',
            field=models.IntegerField(db_index=True, default=0),
        ),
        migrations.AlterField(
            model_name='slip',
            name='played_at',
            field=models.DateTimeField(db_index=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='slip',
            name='slip_token',
            field=models.CharField(db_index=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='team',
            name='name',
            field=models.CharField(db_index=True, max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='weekendraffle',
            name='is_active',
            field=models.BooleanField(db_index=True, default=False),
        ),
        migrations.AlterField(
            model_name='weekendraffle',
            name='live',
            field=models.BooleanField(db_index=True, default=False),
        ),
    ]