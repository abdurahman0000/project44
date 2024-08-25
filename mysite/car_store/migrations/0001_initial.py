# Generated by Django 5.1 on 2024-08-25 08:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marka',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marka_name', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(max_length=26)),
                ('markas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car_store.marka')),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_name', models.CharField(max_length=22)),
                ('description', models.TextField()),
                ('year', models.PositiveIntegerField(default=0)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('color', models.CharField(max_length=16)),
                ('volume', models.FloatField(default=0)),
                ('markakey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car_store.marka')),
                ('modelkey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car_store.model')),
            ],
        ),
    ]