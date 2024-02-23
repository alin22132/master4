# Generated by Django 4.2.5 on 2024-02-06 19:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.TextField(default='def_category_img')),
            ],
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('Brand', models.ForeignKey(default='default_brand', on_delete=django.db.models.deletion.CASCADE, related_name='models', to='home.brand')),
            ],
        ),
        migrations.CreateModel(
            name='Item_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.TextField(default='def_item_img')),
                ('price', models.FloatField(default=0.0)),
                ('Model', models.IntegerField(default=1)),
            ],
        ),
        migrations.AddField(
            model_name='brand',
            name='category',
            field=models.ForeignKey(default='default_category', on_delete=django.db.models.deletion.CASCADE, related_name='brands', to='home.category'),
        ),
    ]
