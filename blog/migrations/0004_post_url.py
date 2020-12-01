# Generated by Django 3.1.2 on 2020-10-15 12:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20201015_1118'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='url',
            field=models.SlugField(default=django.utils.timezone.now, unique=True),
            preserve_default=False,
        ),
    ]
