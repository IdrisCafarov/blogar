# Generated by Django 4.1.5 on 2023-02-06 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_instructor'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='instructor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='blog', to='blog.instructor'),
        ),
    ]