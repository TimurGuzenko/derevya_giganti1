# Generated by Django 4.1.7 on 2023-07-06 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0006_alter_customer_email'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Women',
            new_name='Product',
        ),
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
