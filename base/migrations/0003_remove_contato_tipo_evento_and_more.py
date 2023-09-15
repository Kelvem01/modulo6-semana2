# Generated by Django 4.2.5 on 2023-09-14 20:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0002_contato_tipo_evento"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="contato",
            name="tipo_evento",
        ),
        migrations.AddField(
            model_name="contato",
            name="preferencia_evento",
            field=models.CharField(
                choices=[
                    ("todos", "Todos"),
                    ("musicais", "Eventos Musicais"),
                    ("esportivos", "Eventos Esportivos"),
                    ("educativos", "Eventos Educativos"),
                ],
                default="todos",
                max_length=50,
                verbose_name="Preferencia de Eventos",
            ),
        ),
    ]
