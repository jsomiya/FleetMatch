# Generated by Django 3.1.2 on 2020-11-02 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0004_auto_20201102_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='company_id',
            field=models.EmailField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='registration',
            name='company_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='registration',
            name='description',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='registration',
            name='services',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
    ]
