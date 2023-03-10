# Generated by Django 4.1.5 on 2023-01-25 12:46

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_blog_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='content',
        ),
        migrations.AddField(
            model_name='blog',
            name='image_1',
            field=models.ImageField(blank=True, null=True, upload_to='blogs'),
        ),
        migrations.AddField(
            model_name='blog',
            name='image_2',
            field=models.ImageField(blank=True, null=True, upload_to='blogs'),
        ),
        migrations.AddField(
            model_name='blog',
            name='image_3',
            field=models.ImageField(blank=True, null=True, upload_to='blogs'),
        ),
        migrations.AddField(
            model_name='blog',
            name='text_1',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='text_2',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='text_3',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
