# Generated by Django 3.2.3 on 2021-06-18 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_rename_project_type_personalproject_project_visibility'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalproject',
            name='future_development_notes',
            field=models.TextField(default=''),
        ),
    ]
