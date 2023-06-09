# Generated by Django 4.1.4 on 2023-05-07 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_rename_link_courselinks_access_code_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='courselinks',
            name='use_access_code',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='courselinks',
            name='access_code',
            field=models.CharField(db_index=True, max_length=255, unique=True),
        ),
    ]
