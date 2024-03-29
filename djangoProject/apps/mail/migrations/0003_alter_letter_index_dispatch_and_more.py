# Generated by Django 5.0.2 on 2024-03-04 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0002_letter_is_given_parcel_is_given'),
    ]

    operations = [
        migrations.AlterField(
            model_name='letter',
            name='index_dispatch',
            field=models.IntegerField(verbose_name='Индекс места отправки'),
        ),
        migrations.AlterField(
            model_name='letter',
            name='index_receipt',
            field=models.IntegerField(verbose_name='Индекс места получения'),
        ),
        migrations.AlterField(
            model_name='parcel',
            name='index_dispatch',
            field=models.IntegerField(verbose_name='Индекс места отправки'),
        ),
        migrations.AlterField(
            model_name='parcel',
            name='index_receipt',
            field=models.IntegerField(verbose_name='Индекс места получения'),
        ),
    ]
