# Generated by Django 5.0.6 on 2024-11-23 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_alter_file_file_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='code',
            field=models.TextField(default=''),
        ),
    ]
