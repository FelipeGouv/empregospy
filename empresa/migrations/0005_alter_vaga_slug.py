# Generated by Django 4.0.4 on 2022-04-27 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0004_vaga_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vaga',
            name='slug',
            field=models.SlugField(blank=True, max_length=1000, null=True, unique=True, verbose_name='slug'),
        ),
    ]