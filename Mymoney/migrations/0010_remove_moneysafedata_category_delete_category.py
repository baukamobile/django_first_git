# Generated by Django 4.2.7 on 2024-03-04 07:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Mymoney', '0009_rename_cat_moneysafedata_category_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='moneysafedata',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]