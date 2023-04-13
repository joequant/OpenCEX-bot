# Generated by Django 3.2.18 on 2023-04-13 08:36

import django.contrib.postgres.fields
from django.db import migrations, models


def transfer_precisions(apps, schema_editor):
    PairSettings = apps.get_model('core', 'PairSettings')
    precisions_map = {
        'BTC-USDT': ['100', '10', '1', '0.1', '0.01'],
        'ETH-USDT': ['100', '10', '1', '0.1', '0.01'],
        'TRX-USDT': ['0.01', '0.001', '0.0001', '0.00001'],
        'BNB-USDT': ['100', '10', '1', '0.1', '0.01'],
    }
    for pair, precisions in precisions_map.items():
        PairSettings.objects.filter(pair=pair).update(precisions=precisions)


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_pairsettings_enable_alerts'),
    ]

    operations = [
        migrations.AddField(
            model_name='coininfo',
            name='logo',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='pairsettings',
            name='precisions',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=16), default=list, size=None),
        ),
        migrations.RunPython(transfer_precisions),
    ]
