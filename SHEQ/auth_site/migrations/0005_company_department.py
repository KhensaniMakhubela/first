# Generated by Django 4.1.6 on 2023-02-25 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_site', '0004_status_process_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='department',
            field=models.ManyToManyField(blank=True, null=True, to='auth_site.department'),
        ),
    ]