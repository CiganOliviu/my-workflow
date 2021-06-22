# Generated by Django 3.2.3 on 2021-06-20 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0011_alter_personalproject_future_development_notes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organizations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=25)),
                ('gmail', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('url', models.URLField()),
            ],
        ),
    ]