# Generated by Django 4.2.3 on 2023-07-27 00:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_data', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='autor',
            old_name='name_autor',
            new_name='nome',
        ),
    ]
