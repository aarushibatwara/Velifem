# Generated by Django 4.0.6 on 2023-03-23 06:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('velifem', '0005_alter_adoption_breed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donation',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='donation',
            name='currency',
        ),
        migrations.RemoveField(
            model_name='donation',
            name='donation_type',
        ),
        migrations.RemoveField(
            model_name='donation',
            name='other_purpose',
        ),
        migrations.RemoveField(
            model_name='donation',
            name='payment_method',
        ),
        migrations.RemoveField(
            model_name='donation',
            name='purpose',
        ),
    ]
