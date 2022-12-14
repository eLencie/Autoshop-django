# Generated by Django 3.2.6 on 2022-11-20 08:34

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_remove_invoice_total_cost'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Countries',
            new_name='Country',
        ),
        migrations.RenameModel(
            old_name='Goods',
            new_name='Good',
        ),
        migrations.RenameModel(
            old_name='Groups',
            new_name='Group',
        ),
        migrations.RenameModel(
            old_name='Units',
            new_name='Unit',
        ),
        migrations.RenameModel(
            old_name='Banks',
            new_name='Bank',
        ),
        migrations.CreateModel(
            name='Contractor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('okonh', models.CharField(blank=True, max_length=5, null=True)),
                ('okpo', models.CharField(blank=True, max_length=10, null=True)),
                ('inn', models.CharField(blank=True, max_length=23, null=True)),
                ('is_supplier', models.BooleanField()),
                ('comment', models.CharField(blank=True, max_length=150, null=True)),
                ('bank', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='shop.bank', verbose_name='Банк')),
            ],
        ),
    ]
