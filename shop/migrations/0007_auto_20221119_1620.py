# Generated by Django 3.2.6 on 2022-11-19 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_alter_gooditem_cost'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='invoice',
            options={'ordering': ('-pk',)},
        ),
        migrations.RenameField(
            model_name='gooditem',
            old_name='cost',
            new_name='price',
        ),
        migrations.AlterField(
            model_name='invoice',
            name='comment',
            field=models.CharField(blank=True, default='Simple sale', max_length=250, null=True),
        ),
    ]
