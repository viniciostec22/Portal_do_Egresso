# Generated by Django 4.1.7 on 2023-04-25 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apresentacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=15)),
                ('texto_esquerdo', models.CharField(max_length=40, verbose_name='Texto esquerda')),
                ('texto_direita', models.TextField(verbose_name='texto direita')),
            ],
        ),
    ]