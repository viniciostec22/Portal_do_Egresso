# Generated by Django 4.1.7 on 2023-05-02 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0023_contato_enviado_boas_vindas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='depoimento',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='img_perfil/'),
        ),
        migrations.AlterField(
            model_name='slaider',
            name='img',
            field=models.ImageField(upload_to='img/'),
        ),
    ]
