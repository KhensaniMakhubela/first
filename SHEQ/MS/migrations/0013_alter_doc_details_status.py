# Generated by Django 4.1.6 on 2023-02-19 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MS', '0012_alter_doc_details_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doc_details',
            name='status',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
