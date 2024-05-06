# Generated by Django 5.0.3 on 2024-04-08 13:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tarefas', '0003_remove_tarefas_descricao_completa_and_more'),
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarefas',
            name='tarefa_para',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='usuario.usuario'),
        ),
    ]