# Generated by Django 5.1.6 on 2025-03-10 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_plant_category_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conatct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fisrt_name', models.CharField(max_length=512)),
                ('last_name', models.CharField(max_length=512)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
