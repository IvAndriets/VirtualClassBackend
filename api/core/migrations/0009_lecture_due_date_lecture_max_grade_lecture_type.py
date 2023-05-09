# Generated by Django 4.1.4 on 2023-05-09 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_studentscourse_course_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecture',
            name='due_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='lecture',
            name='max_grade',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='lecture',
            name='type',
            field=models.CharField(choices=[('lecture', 'lecture'), ('lab', 'lab')], default='lecture', max_length=10),
        ),
    ]
