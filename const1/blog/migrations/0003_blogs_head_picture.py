# Generated by Django 4.2.3 on 2023-07-21 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_dasteh_bandy_model_slug_alter_tag_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs',
            name='head_picture',
            field=models.FileField(null=True, upload_to='Images_Blog/', verbose_name='عکس سر تیتر '),
        ),
    ]
