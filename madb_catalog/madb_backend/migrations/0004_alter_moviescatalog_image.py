# Generated by Django 4.0.3 on 2024-03-28 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('madb_backend', '0003_alter_moviescatalog_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviescatalog',
            name='image',
            field=models.ImageField(upload_to='movies/'),
        ),
    ]