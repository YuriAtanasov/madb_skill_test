# Generated by Django 5.0.3 on 2024-03-29 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('madb_backend', '0012_alter_moviescatalog_moviesynopsis'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviescatalog',
            name='genre',
            field=models.CharField(choices=[('Action', 'ACTION'), ('Drama', 'DRAMA'), ('Comedy', 'COMEDY'), ('Romance', 'ROMANCE')], max_length=7),
        ),
    ]
