# Generated by Django 4.2.5 on 2023-09-09 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0002_userprofile_birthdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='description',
            field=models.TextField(null=True),
        ),
    ]