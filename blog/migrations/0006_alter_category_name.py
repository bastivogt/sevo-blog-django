# Generated by Django 5.0.4 on 2024-05-03 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_author_alter_mediaimage_image_post_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(db_index=True, max_length=100, unique=True),
        ),
    ]