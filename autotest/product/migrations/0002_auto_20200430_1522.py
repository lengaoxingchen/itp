# Generated by Django 2.1.3 on 2020-04-30 07:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='create_name',
            new_name='create_time',
        ),
    ]
