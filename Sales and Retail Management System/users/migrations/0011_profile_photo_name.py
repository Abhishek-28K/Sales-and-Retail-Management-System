# Generated by Django 5.0.1 on 2024-03-23 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_profile_photo_delete_profilephoto'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile_photo',
            name='Name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
