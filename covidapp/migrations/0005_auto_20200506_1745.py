# Generated by Django 2.0.7 on 2020-05-06 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covidapp', '0004_auto_20200506_0112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospital',
            name='hospital_currently',
            field=models.IntegerField(),
        ),
    ]