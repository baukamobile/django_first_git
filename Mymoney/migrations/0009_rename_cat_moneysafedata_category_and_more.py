# Generated by Django 4.2.7 on 2024-03-04 07:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Mymoney', '0008_rename_category_moneysafedata_categories'),
    ]

    operations = [
        migrations.RenameField(
            model_name='moneysafedata',
            old_name='cat',
            new_name='category',
        ),
        migrations.RemoveField(
            model_name='moneysafedata',
            name='categories',
        ),
    ]
