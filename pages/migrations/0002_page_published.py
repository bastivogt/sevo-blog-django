# Generated by Django 5.0.4 on 2024-05-03 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='published',
            field=models.BooleanField(default=True),
        ),
    ]
