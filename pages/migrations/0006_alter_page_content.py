# Generated by Django 5.0.4 on 2024-05-07 23:27

import tinymce.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_page_template'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='content',
            field=tinymce.models.HTMLField(),
        ),
    ]
