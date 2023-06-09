# Generated by Django 4.1.4 on 2023-05-11 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_lecturefiles'),
    ]

    operations = [
        migrations.AddField(
            model_name='fileinfo',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='lecture',
            name='files',
            field=models.ManyToManyField(to='core.fileinfo'),
        ),
        migrations.DeleteModel(
            name='LectureFiles',
        ),
    ]
