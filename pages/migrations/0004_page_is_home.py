# Generated by Django 5.0.4 on 2024-05-04 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_remove_page_menus_menu_pages'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='is_home',
            field=models.BooleanField(default=False),
        ),
    ]
