# Generated by Django 4.1.5 on 2023-01-31 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tabelaInt', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tabelaint',
            name='tabela',
            field=models.CharField(choices=[('000', 'Selecionar...'), ('001', 'Tabela Estado'), ('002', 'Tabela Cor'), ('003', 'Tabela Tamanho'), ('100', 'Tabela Categoria')], default='000', max_length=3),
        ),
    ]
