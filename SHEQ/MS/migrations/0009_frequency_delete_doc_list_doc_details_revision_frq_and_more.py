# Generated by Django 4.1.6 on 2023-02-19 09:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MS', '0008_alter_doc_details_procedure_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Frequency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('months', models.IntegerField(max_length=3)),
            ],
        ),
        migrations.DeleteModel(
            name='Doc_list',
        ),
        migrations.AddField(
            model_name='doc_details',
            name='revision_frq',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='MS.frequency'),
        ),
        migrations.AddField(
            model_name='document',
            name='revision_frq',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='MS.frequency'),
        ),
    ]
