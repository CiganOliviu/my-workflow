# Generated by Django 3.2.3 on 2021-06-28 19:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0016_portfolio'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='details',
            field=models.TextField(default='None'),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='future_development_notes',
            field=models.TextField(default='None'),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='github_url',
            field=models.URLField(default='None'),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='name',
            field=models.CharField(default='None', max_length=50),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='stack',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='projects.developmentstack'),
        ),
    ]