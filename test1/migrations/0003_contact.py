# Generated by Django 5.0.1 on 2024-02-07 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test1', '0002_product_product_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.CharField(max_length=1000)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]