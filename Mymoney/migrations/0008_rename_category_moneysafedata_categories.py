# Generated by Django 4.2.7 on 2024-03-04 07:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Mymoney', '0007_alter_moneysafedata_cat'),
    ]

    operations = [
        migrations.RenameField(
            model_name='moneysafedata',
            old_name='category',
            new_name='categories',
        ),
    ]