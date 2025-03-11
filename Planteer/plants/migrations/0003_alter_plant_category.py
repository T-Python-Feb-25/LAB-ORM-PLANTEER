# Generated by Django 4.2.19 on 2025-03-10 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0002_plant_related_plants'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='category',
            field=models.CharField(choices=[('Flowers', 'Flowers'), ('Trees', 'Trees'), ('Shrubs', 'Shrubs'), ('Herbs', 'Herbs'), ('Vegetables', 'Vegetables'), ('Fruits', 'Fruits')], max_length=50),
        ),
    ]
