# Generated by Django 3.2.7 on 2021-09-21 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0005_auto_20210921_1908"),
    ]

    operations = [
        migrations.AlterField(
            model_name="estudiante",
            name="first_name",
            field=models.CharField(
                blank=True, max_length=128, null=True, verbose_name="Nombre"
            ),
        ),
        migrations.AlterField(
            model_name="estudiante",
            name="last_name",
            field=models.CharField(
                blank=True, max_length=128, null=True, verbose_name="Apellido"
            ),
        ),
    ]
