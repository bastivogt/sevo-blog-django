# Generated by Django 5.0.4 on 2024-05-07 23:27

import tinymce.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_post_allow_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=tinymce.models.HTMLField(),
        ),
    ]