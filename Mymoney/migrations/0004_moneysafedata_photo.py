# Generated by Django 4.2.7 on 2024-03-03 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mymoney', '0003_remove_moneysafedata_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='moneysafedata',
            name='photo',
            field=models.ImageField(default=None, upload_to='photos/%Y/%m/%d/'),
            preserve_default=False,
        ),
    ]
