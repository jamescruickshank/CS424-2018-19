# Generated by Django 2.1.1 on 2018-10-08 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubmanager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
    ]
