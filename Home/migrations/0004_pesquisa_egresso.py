# Generated by Django 4.1.7 on 2023-04-26 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0003_alter_apresentacao_texto_esquerdo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pesquisa_Egresso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=15)),
                ('texto', models.TextField(verbose_name='texto')),
                ('subtitulo', models.CharField(max_length=15, verbose_name='Subtitulo')),
                ('texto_direita', models.TextField(verbose_name='texto direita')),
            ],
        ),
    ]
