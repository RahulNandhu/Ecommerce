# Generated by Django 5.0 on 2024-01-30 08:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('desc', models.TextField()),
                ('price', models.IntegerField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='product')),
                ('stock', models.IntegerField()),
                ('availability', models.BooleanField(default=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.items')),
            ],
        ),
    ]
