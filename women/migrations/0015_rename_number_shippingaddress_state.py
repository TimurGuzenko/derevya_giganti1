# Generated by Django 4.1.7 on 2023-07-11 10:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0014_rename_state_shippingaddress_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='number',
            new_name='state',
        ),
    ]