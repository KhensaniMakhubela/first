# Generated by Django 4.1.6 on 2023-02-18 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MS', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ms_menu',
            name='clause_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='procedure',
            name='company',
            field=models.CharField(max_length=20),
        ),
    ]