# Generated by Django 5.2.1 on 2025-05-29 15:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wine_wiki', '0002_ingest_wine_categories'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wine',
            name='slug',
        ),
    ]
