# Generated by Django 4.1 on 2022-09-07 22:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('company', models.CharField(max_length=100)),
                ('secret', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.CharField(max_length=512, unique=True)),
                ('amount', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('status', models.CharField(choices=[('New', 'New'), ('Completed', 'Completed'), ('Rejected', 'Rejected')], max_length=128)),
                ('currency', models.CharField(choices=[('RUB', 'RUB'), ('USD', 'USD')], max_length=32)),
                ('data', models.CharField(max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512, unique=True)),
                ('value', models.FloatField()),
                ('currency', models.CharField(choices=[('RUB', 'RUB'), ('USD', 'USD')], default='RUB', max_length=32)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billing.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Balance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(default=0.0)),
                ('currency', models.CharField(choices=[('RUB', 'RUB'), ('USD', 'USD')], max_length=32)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billing.customer')),
            ],
        ),
    ]
