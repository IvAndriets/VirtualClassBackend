# Generated by Django 4.1.4 on 2023-05-14 06:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_rename_files_homeworks_file_homeworks_mark_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='homeworks',
            unique_together={('lecture', 'owner')},
        ),
    ]
