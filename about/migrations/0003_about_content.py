# Generated by Django 4.2.16 on 2024-11-21 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_about_updated_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='content',
            field=models.TextField(default='Default content'),
        ),
    ]
