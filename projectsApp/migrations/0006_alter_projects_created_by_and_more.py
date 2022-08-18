# Generated by Django 4.1 on 2022-08-18 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectsApp', '0005_alter_projects_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='created_by',
            field=models.CharField(max_length=225, null=True),
        ),
        migrations.AlterField(
            model_name='projects',
            name='project_priority',
            field=models.CharField(max_length=225, null=True),
        ),
        migrations.AlterField(
            model_name='projects',
            name='project_progress',
            field=models.CharField(max_length=225),
        ),
        migrations.AlterField(
            model_name='projects',
            name='project_title',
            field=models.CharField(max_length=225),
        ),
    ]
