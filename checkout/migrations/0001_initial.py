# Generated by Django 3.2 on 2021-05-09 07:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),  # noqa:501
                ('order_number', models.CharField(editable=False, max_length=35)),   # noqa:501
                ('total', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='USD Order Total')),   # noqa:501
                ('order_total', models.DecimalField(decimal_places=2, default=0, max_digits=8)),   # noqa:501
                ('delivery_cost', models.DecimalField(decimal_places=2, default=0, max_digits=8)),   # noqa:501
                ('emailAddress', models.EmailField(blank=True, max_length=250, verbose_name='Email Adress')),   # noqa:501
                ('created', models.DateTimeField(auto_now_add=True)),
                ('billingName', models.CharField(blank=True, max_length=250)),   # noqa:501
                ('billingAdress1', models.CharField(blank=True, max_length=250)),   # noqa:501
                ('billingCity', models.CharField(blank=True, max_length=250)),
                ('billingPostcode', models.CharField(blank=True, max_length=250)),   # noqa:501
                ('billingCountry', models.CharField(blank=True, max_length=250)),   # noqa:501
                ('shippingName', models.CharField(blank=True, max_length=250)),
                ('shippingAddress1', models.CharField(blank=True, max_length=250)),   # noqa:501
                ('shippingCity', models.CharField(blank=True, max_length=250)),
                ('shippingPostcode', models.CharField(blank=True, max_length=250)),   # noqa:501
                ('shippingCountry', models.CharField(blank=True, max_length=250)),   # noqa:501
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),   # noqa:501
                ('product', models.CharField(max_length=250)),
                ('quantity', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='USD Price')),   # noqa:501
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='checkout.order')),   # noqa:501
            ],
            options={
                'db_table': 'OrderItem',
            },
        ),
    ]
