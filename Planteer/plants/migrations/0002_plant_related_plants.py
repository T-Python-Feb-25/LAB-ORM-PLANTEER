# Generated by Django 4.2.19 on 2025-03-10 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='plant',
            name='related_plants',
            field=models.ManyToManyField(blank=True, to='plants.plant'),
        ),
    ]
