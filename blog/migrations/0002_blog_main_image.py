# Generated by Django 4.1.5 on 2023-01-21 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='main_image',
            field=models.ImageField(null=True, upload_to='blogs'),
        ),
    ]
