# Generated by Django 4.1.6 on 2023-02-18 11:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth_site', '0002_alter_user_added_info_company_and_more'),
        ('MS', '0003_doc_type_procedure_document_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='procedure',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth_site.company'),
        ),
    ]