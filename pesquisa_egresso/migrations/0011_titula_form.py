# Generated by Django 4.1.7 on 2023-05-17 02:34

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pesquisa_egresso', '0010_alter_pesquisa_contribuicao_monitor_estagio_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Titula_Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', ckeditor.fields.RichTextField(max_length=50, verbose_name='titulo')),
            ],
        ),
    ]
