# Generated by Django 4.0.4 on 2022-04-27 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0003_vaga_ativa_alter_vaga_candidatos'),
    ]

    operations = [
        migrations.AddField(
            model_name='vaga',
            name='slug',
            field=models.SlugField(default='1-estoque', max_length=1000, unique=True, verbose_name='slug'),
            preserve_default=False,
        ),
    ]
