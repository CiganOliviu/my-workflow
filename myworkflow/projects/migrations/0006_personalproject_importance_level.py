# Generated by Django 3.2.3 on 2021-06-18 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_universityclasses'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalproject',
            name='importance_level',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
