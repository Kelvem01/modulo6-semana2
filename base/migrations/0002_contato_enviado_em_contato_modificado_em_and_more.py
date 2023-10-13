# Generated by Django 4.2.5 on 2023-10-04 18:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="contato",
            name="enviado_em",
            field=models.DateTimeField(
                auto_now_add=True, null=True, verbose_name="Enviado em"
            ),
        ),
        migrations.AddField(
            model_name="contato",
            name="modificado_em",
            field=models.DateTimeField(auto_now=True, verbose_name="Modificado em"),
        ),
        migrations.AlterField(
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
                max_length=20,
                verbose_name="Preferência de Eventos",
            ),
        ),
    ]