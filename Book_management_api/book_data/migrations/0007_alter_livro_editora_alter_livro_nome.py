# Generated by Django 4.2.3 on 2023-08-02 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_data', '0006_alter_autor_genero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livro',
            name='editora',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='livro',
            name='nome',
            field=models.CharField(max_length=100),
        ),
    ]