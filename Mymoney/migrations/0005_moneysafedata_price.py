# Generated by Django 4.2.7 on 2024-03-03 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mymoney', '0004_moneysafedata_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='moneysafedata',
            name='price',
            field=models.IntegerField(default=None, max_length=100),
            preserve_default=False,
        ),
    ]
