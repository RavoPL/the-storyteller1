# Generated by Django 3.2.19 on 2023-12-15 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20231215_2152'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='slug',
            field=models.SlugField(default=1, max_length=200, unique=True),
            preserve_default=False,
        ),
    ]
