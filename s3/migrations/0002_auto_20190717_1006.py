# Generated by Django 2.2.3 on 2019-07-17 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('s3', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bucket',
            name='access_key',
            field=models.CharField(default='', max_length=16),
        ),
        migrations.AddField(
            model_name='bucket',
            name='secret_key',
            field=models.CharField(default='', max_length=128),
        ),
    ]
