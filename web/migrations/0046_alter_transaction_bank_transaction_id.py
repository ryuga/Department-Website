# Generated by Django 4.0 on 2021-12-22 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0045_subevents_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='bank_transaction_id',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]
