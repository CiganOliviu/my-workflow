# Generated by Django 3.2.3 on 2021-05-24 20:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_rename_computerscienceprojects_personalprojects'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PersonalProjects',
            new_name='PersonalProject',
        ),
        migrations.RenameModel(
            old_name='UniversityProjects',
            new_name='UniversityProject',
        ),
    ]
