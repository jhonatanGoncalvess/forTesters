# Generated by Django 3.0.3 on 2020-05-30 23:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cenario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('descricao', models.TextField()),
                ('criticidade', models.CharField(choices=[('Alta', 'Alta'), ('Baixa', 'Baixa'), ('Média', 'Média'), ('Altíssima', 'Altíssima'), ('Baixíssima', 'Baixíssima')], max_length=11, verbose_name='Criticidade')),
                ('resultado_esperado', models.TextField()),
                ('resultado_obtido', models.TextField()),
                ('data_criacao', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Projeto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, verbose_name='Nome')),
                ('descricao', models.TextField(verbose_name='Descrição')),
                ('status', models.CharField(choices=[('Em Desenvolvimento', 'Em Desenvolvimento'), ('Em Homologação', 'Em Homologação'), ('Finalizado', 'Finalizado'), ('Não Iniciado', 'Não Iniciado')], max_length=20, verbose_name='Status')),
                ('data_criacao', models.DateTimeField(default=django.utils.timezone.now)),
                ('responsavel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Responsável')),
            ],
        ),
        migrations.CreateModel(
            name='Roteiro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('descricao', models.TextField()),
                ('status', models.CharField(choices=[('Aprovado', 'Aprovado'), ('Em Teste', 'Em Teste'), ('Reprovado', 'Reprovado')], max_length=10, verbose_name='Status')),
                ('data_criacao', models.DateTimeField(default=django.utils.timezone.now)),
                ('cenarios', models.ManyToManyField(to='for_testers.Cenario')),
                ('projetos', models.ManyToManyField(to='for_testers.Projeto')),
                ('responsavel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
