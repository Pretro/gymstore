# Generated by Django 3.2 on 2021-06-11 07:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_product_has_sizes'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductSize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),  # noqa:501
                ('name', models.CharField(max_length=250)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),  # noqa:501
            ],
            options={
                'verbose_name': 'Size',
                'verbose_name_plural': 'Sizes',
                'ordering': ('name',),
            },
        ),
    ]
