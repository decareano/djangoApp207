# Generated by Django 2.0.7 on 2020-05-13 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covidapp', '0005_auto_20200511_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospital',
            name='dead_daily',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='hospital_currently',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='hospital_increase',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='icucurrently',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='tested_today',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
