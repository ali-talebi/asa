# Generated by Django 4.2.3 on 2023-07-27 14:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_comments_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='time',
        ),
    ]
