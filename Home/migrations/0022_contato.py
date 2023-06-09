# Generated by Django 4.1.7 on 2023-05-01 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0021_politica_remove_depoimento_nivel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('telefone', models.CharField(max_length=11, verbose_name='Telefone')),
            ],
        ),
    ]
