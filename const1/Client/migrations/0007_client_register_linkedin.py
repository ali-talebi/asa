# Generated by Django 4.2.3 on 2023-07-29 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Client', '0006_client_register_fields'),
    ]

    operations = [
        migrations.AddField(
            model_name='client_register',
            name='linkedin',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='لینک توئیتر'),
        ),
    ]