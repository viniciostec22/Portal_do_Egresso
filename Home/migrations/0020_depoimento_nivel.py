# Generated by Django 4.1.7 on 2023-04-28 18:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0019_remove_depoimento_nivel'),
    ]

    operations = [
        migrations.AddField(
            model_name='depoimento',
            name='nivel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Home.nivel_curso'),
        ),
    ]
