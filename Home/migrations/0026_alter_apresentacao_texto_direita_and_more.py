# Generated by Django 4.1.7 on 2023-05-17 01:23

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0025_mensagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apresentacao',
            name='texto_direita',
            field=ckeditor.fields.RichTextField(verbose_name='texto direita'),
        ),
        migrations.AlterField(
            model_name='apresentacao',
            name='texto_esquerdo',
            field=ckeditor.fields.RichTextField(max_length=40, verbose_name='Texto esquerda'),
        ),
    ]