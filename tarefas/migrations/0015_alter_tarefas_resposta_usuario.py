# Generated by Django 5.0.3 on 2024-06-01 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tarefas', '0014_tarefas_resposta_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarefas',
            name='resposta_usuario',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]