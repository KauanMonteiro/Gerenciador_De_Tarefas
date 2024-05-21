# Generated by Django 5.0.3 on 2024-05-21 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tarefas', '0010_tarefas_alternativa1_tarefas_alternativa2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarefas',
            name='alternativa1',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tarefas',
            name='alternativa2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tarefas',
            name='alternativa3',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tarefas',
            name='alternativa4',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tarefas',
            name='alternativa5',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tarefas',
            name='alternativa_correta',
            field=models.IntegerField(blank=True, choices=[(1, 'A'), (2, 'B'), (3, 'C'), (4, 'D'), (5, 'E')], null=True),
        ),
        migrations.AlterField(
            model_name='tarefas',
            name='descricao',
            field=models.TextField(blank=True, null=True),
        ),
    ]