# Generated by Django 4.2.5 on 2024-02-09 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_item_list_art_nr'),
    ]

    operations = [
        migrations.AddField(
            model_name='item_list',
            name='avlbl',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='item_list',
            name='descr',
            field=models.TextField(default='N/A'),
        ),
    ]
