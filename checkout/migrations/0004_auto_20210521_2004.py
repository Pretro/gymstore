# Generated by Django 3.2 on 2021-05-21 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_auto_20210515_0717'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='original_cart',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='order',
            name='stripe_pid',
            field=models.CharField(default='', max_length=254),
        ),
    ]
