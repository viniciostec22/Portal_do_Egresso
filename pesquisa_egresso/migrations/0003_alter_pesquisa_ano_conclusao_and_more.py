# Generated by Django 4.1.7 on 2023-05-16 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pesquisa_egresso', '0002_pesquisa_remove_dificuldadestrabalho_egresso_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pesquisa',
            name='ano_conclusao',
            field=models.PositiveIntegerField(verbose_name='Ano de Conclusão'),
        ),
        migrations.AlterField(
            model_name='pesquisa',
            name='avaliacao_aprendizado',
            field=models.PositiveIntegerField(verbose_name='Avaliação Aprendizado'),
        ),
        migrations.AlterField(
            model_name='pesquisa',
            name='avaliacao_curso',
            field=models.PositiveIntegerField(verbose_name='Avaliação Curso'),
        ),
        migrations.AlterField(
            model_name='pesquisa',
            name='contribuicao_monitor_estagio',
            field=models.TextField(verbose_name='Contribuição monitor estagio'),
        ),
        migrations.AlterField(
            model_name='pesquisa',
            name='endereco',
            field=models.CharField(max_length=200, verbose_name='Endereço'),
        ),
        migrations.AlterField(
            model_name='pesquisa',
            name='experiencias_if',
            field=models.TextField(verbose_name='Experiencias IF'),
        ),
        migrations.AlterField(
            model_name='pesquisa',
            name='instituicao',
            field=models.CharField(max_length=100, verbose_name='Instituição'),
        ),
        migrations.AlterField(
            model_name='pesquisa',
            name='participacao_extensao',
            field=models.BooleanField(verbose_name='Participação Projeto de Extenção'),
        ),
        migrations.AlterField(
            model_name='pesquisa',
            name='participacao_pesquisa',
            field=models.BooleanField(verbose_name='Participação Projeto de Pesquisa'),
        ),
        migrations.AlterField(
            model_name='pesquisa',
            name='realizacao_estagios',
            field=models.BooleanField(verbose_name='Realização de Estagio'),
        ),
        migrations.AlterField(
            model_name='pesquisa',
            name='sexo',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='pesquisa',
            name='sugestoes_homepage',
            field=models.TextField(verbose_name='Sugestões homepage'),
        ),
        migrations.AlterField(
            model_name='pesquisa',
            name='sugestoes_relacao',
            field=models.TextField(verbose_name='Sugestões relação'),
        ),
        migrations.AlterField(
            model_name='pesquisa',
            name='trabalho_area_formacao',
            field=models.CharField(max_length=100, verbose_name='Trabalho Aréa Formação'),
        ),
    ]