# Generated by Django 3.2.3 on 2021-06-28 19:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0018_rename_portfolio_portfolioproject'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CurrentReadingBook',
        ),
    ]
