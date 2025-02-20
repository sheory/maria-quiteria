# Generated by Django 4.1.5 on 2023-01-03 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("datasets", "0029_file_local_path"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="historicalcitycouncilattendancelist",
            options={
                "get_latest_by": ("history_date", "history_id"),
                "ordering": ("-history_date", "-history_id"),
                "verbose_name": "historical Câmara de Vereadores - Lista de Presença",
                "verbose_name_plural": "historical Câmara de Vereadores - Listas de Presença",
            },
        ),
        migrations.AlterModelOptions(
            name="historicalcitycouncilbid",
            options={
                "get_latest_by": ("history_date", "history_id"),
                "ordering": ("-history_date", "-history_id"),
                "verbose_name": "historical Câmara de Vereadores - Licitação",
                "verbose_name_plural": "historical Câmara de Vereadores - Licitações",
            },
        ),
        migrations.AlterModelOptions(
            name="historicalcitycouncilcontract",
            options={
                "get_latest_by": ("history_date", "history_id"),
                "ordering": ("-history_date", "-history_id"),
                "verbose_name": "historical Câmara de Vereadores - Contrato",
                "verbose_name_plural": "historical Câmara de Vereadores - Contratos",
            },
        ),
        migrations.AlterModelOptions(
            name="historicalcitycouncilexpense",
            options={
                "get_latest_by": ("history_date", "history_id"),
                "ordering": ("-history_date", "-history_id"),
                "verbose_name": "historical Câmara de Vereadores - Despesa",
                "verbose_name_plural": "historical Câmara de Vereadores - Despesas",
            },
        ),
        migrations.AlterModelOptions(
            name="historicalcitycouncilrevenue",
            options={
                "get_latest_by": ("history_date", "history_id"),
                "ordering": ("-history_date", "-history_id"),
                "verbose_name": "historical Câmara de Vereadores - Receita",
                "verbose_name_plural": "historical Câmara de Vereadores - Receitas",
            },
        ),
        migrations.AlterField(
            model_name="historicalcitycouncilattendancelist",
            name="history_date",
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name="historicalcitycouncilbid",
            name="history_date",
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name="historicalcitycouncilcontract",
            name="history_date",
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name="historicalcitycouncilexpense",
            name="history_date",
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name="historicalcitycouncilrevenue",
            name="history_date",
            field=models.DateTimeField(db_index=True),
        ),
    ]
