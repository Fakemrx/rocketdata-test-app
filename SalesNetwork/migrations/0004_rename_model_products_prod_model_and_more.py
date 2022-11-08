# Generated by Django 4.1.3 on 2022-11-08 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SalesNetwork', '0003_remove_sellersnetwork_products_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='model',
            new_name='prod_model',
        ),
        migrations.AlterField(
            model_name='sellersnetwork',
            name='debt',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Долг'),
        ),
    ]