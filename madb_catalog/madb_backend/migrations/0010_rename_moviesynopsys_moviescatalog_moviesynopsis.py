# Generated by Django 5.0.3 on 2024-03-29 05:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('madb_backend', '0009_alter_moviescatalog_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='moviescatalog',
            old_name='movieSynopsys',
            new_name='movieSynopsis',
        ),
    ]
