# Generated by Django 4.1 on 2022-08-14 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectsApp', '0004_rename_create_at_projects_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='created_by',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
