# Generated by Django 4.2.3 on 2023-07-21 10:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Total_project', '0004_slider_index_alter_category_slug_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='slider_index',
            old_name='sentnce',
            new_name='sentence',
        ),
    ]