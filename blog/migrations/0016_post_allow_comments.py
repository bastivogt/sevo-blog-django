# Generated by Django 5.0.4 on 2024-05-07 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='allow_comments',
            field=models.BooleanField(default=False),
        ),
    ]
