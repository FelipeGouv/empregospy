# Generated by Django 4.0.4 on 2022-04-27 20:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vaga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cargo', models.CharField(max_length=1000, verbose_name='Cargo')),
                ('salario', models.FloatField(verbose_name='Salário')),
                ('descricao', models.TextField(verbose_name='Descrição')),
                ('candidatos', models.IntegerField(verbose_name='Candidatos')),
                ('criada_em', models.DateField(auto_now_add=True, verbose_name='Criado Em')),
                ('beneficios', models.CharField(max_length=1000, verbose_name='Benefícios')),
                ('qtd_vagas', models.IntegerField(default=1, verbose_name='Quantidade de Vagas')),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresa.empresa')),
            ],
        ),
    ]
