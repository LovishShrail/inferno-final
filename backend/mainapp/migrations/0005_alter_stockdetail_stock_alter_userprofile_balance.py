# Generated by Django 5.1.6 on 2025-03-14 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_alter_userprofile_balance_userstock_delete_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockdetail',
            name='stock',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=10000.0, max_digits=10),
        ),
    ]
