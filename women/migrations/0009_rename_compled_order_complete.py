# Generated by Django 4.1.7 on 2023-07-07 06:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0008_rename_product_women'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='compled',
            new_name='complete',
        ),
    ]
