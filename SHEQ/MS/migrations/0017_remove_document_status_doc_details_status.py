# Generated by Django 4.1.6 on 2023-02-19 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MS', '0016_remove_doc_details_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='status',
        ),
        migrations.AddField(
            model_name='doc_details',
            name='status',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
