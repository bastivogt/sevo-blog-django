# Generated by Django 5.0.4 on 2024-05-02 23:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_category_post_categories'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('nickname', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='mediaimage',
            name='image',
            field=models.ImageField(upload_to='images/blog'),
        ),
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.author'),
        ),
    ]
