# Generated by Django 4.1.7 on 2023-04-26 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0008_rename_link_serviço_rodape_link_servico'),
    ]

    operations = [
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('endereço', models.TextField(verbose_name='Endereço')),
            ],
        ),
        migrations.CreateModel(
            name='Rodape_kinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_link', models.CharField(max_length=30, null=True, verbose_name='Nome do Link')),
                ('links_importantes', models.CharField(max_length=200, verbose_name='URL')),
            ],
        ),
        migrations.CreateModel(
            name='Rodape_servico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('servicos', models.CharField(max_length=150, verbose_name='Serviços')),
                ('link_servico', models.CharField(max_length=200, null=True, verbose_name='URL serviço')),
            ],
        ),
        migrations.DeleteModel(
            name='Rodape',
        ),
    ]
