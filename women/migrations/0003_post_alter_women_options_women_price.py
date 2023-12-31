# Generated by Django 4.1.7 on 2023-07-05 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0002_alter_women_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('content', models.TextField(verbose_name='content')),
            ],
        ),
        migrations.AlterModelOptions(
            name='women',
            options={'ordering': ['id'], 'verbose_name': 'Деревья мира', 'verbose_name_plural': 'Список деревьев'},
        ),
        migrations.AddField(
            model_name='women',
            name='price',
            field=models.IntegerField(null=True, verbose_name='Цена'),
        ),
    ]
