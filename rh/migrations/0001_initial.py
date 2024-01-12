# Generated by Django 3.2.23 on 2024-01-12 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recursos_Humanos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bnome', models.CharField(max_length=35)),
                ('bcelular', models.IntegerField()),
                ('btelefone', models.IntegerField()),
                ('bfax', models.CharField(max_length=15)),
                ('bemail', models.CharField(max_length=29)),
                ('bmorada', models.CharField(max_length=29)),
                ('blocalidade', models.CharField(max_length=29)),
                ('bzona', models.CharField(max_length=20)),
                ('bpais', models.CharField(max_length=20)),
                ('bnuit', models.CharField(max_length=35, unique=True)),
                ('bobserv', models.TextField()),
                ('data', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
