# Generated by Django 4.1.7 on 2023-05-02 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mensagens', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mensagem',
            name='anexo',
            field=models.FileField(blank=True, null=True, upload_to='anexos/'),
        ),
    ]
