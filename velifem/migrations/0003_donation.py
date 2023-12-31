# Generated by Django 4.0.6 on 2023-03-21 06:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('velifem', '0002_adoption_rename_sosrequest_sos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, validators=[django.core.validators.EmailValidator(message='Invalid email format')])),
                ('country', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('country_code', models.CharField(max_length=3)),
                ('contact_number', models.CharField(max_length=10)),
                ('purpose', models.CharField(choices=[('general', 'General Donation'), ('feed', 'To feed the animals'), ('veterinary', 'For veterinary care'), ('building', 'For building homes for animals'), ('other', 'Towards other specific cause')], max_length=20)),
                ('other_purpose', models.CharField(blank=True, max_length=100)),
                ('donation_type', models.CharField(choices=[('one_time', 'One Time Donation'), ('monthly', 'Monthly Donation'), ('quarterly', 'Quarterly Donation'), ('half_yearly', 'Half-Yearly Donation'), ('yearly', 'Yearly Donation')], max_length=20)),
                ('currency', models.CharField(choices=[('USD', 'USD'), ('EUR', 'EUR'), ('JPY', 'JPY'), ('GBP', 'GBP'), ('CHF', 'CHF'), ('CAD', 'CAD'), ('AUD', 'AUD'), ('ZAR', 'ZAR'), ('AED', 'AED'), ('INR', 'INR')], max_length=3)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_method', models.CharField(choices=[('credit_card', 'Credit / Debit Card'), ('e_wallet', 'E-Wallets'), ('upi', 'UPI'), ('money_order', 'Money Order / Demand Draft')], max_length=20)),
                ('notes', models.TextField(blank=True)),
            ],
        ),
    ]
