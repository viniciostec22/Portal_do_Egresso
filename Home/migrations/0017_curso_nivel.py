# Generated by Django 4.1.7 on 2023-04-28 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0016_rename_campus_campi'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='nivel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Home.nivel_curso'),
        ),
    ]
