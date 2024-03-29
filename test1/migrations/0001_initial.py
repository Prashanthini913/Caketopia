# Generated by Django 5.0.1 on 2024-01-31 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.CharField(max_length=30, unique='True')),
                ('product_name', models.CharField(max_length=30)),
                ('product_desc', models.CharField(max_length=400)),
                ('product_category', models.CharField(max_length=100)),
            ],
        ),
    ]
