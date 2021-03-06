# Generated by Django 4.0.4 on 2022-05-18 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0007_candidatosvaga'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresa',
            name='cidade',
            field=models.CharField(blank=True, max_length=1024, null=True, verbose_name='Cidade'),
        ),
        migrations.AddField(
            model_name='empresa',
            name='descricao',
            field=models.TextField(blank=True, null=True, verbose_name='Descrição'),
        ),
        migrations.AddField(
            model_name='empresa',
            name='email',
            field=models.EmailField(blank=True, max_length=100, null=True, verbose_name='E-mail'),
        ),
        migrations.AddField(
            model_name='empresa',
            name='endereco',
            field=models.CharField(blank=True, max_length=1024, null=True, verbose_name='Endereço'),
        ),
        migrations.AddField(
            model_name='empresa',
            name='estado',
            field=models.CharField(blank=True, max_length=2, null=True, verbose_name='Estado'),
        ),
        migrations.AddField(
            model_name='empresa',
            name='telefone',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Telefone'),
        ),
    ]
