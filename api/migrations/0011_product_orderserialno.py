# Generated by Django 2.1 on 2018-09-06 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20180906_1636'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='orderSerialNo',
            field=models.ManyToManyField(blank=True, to='api.OrderSerialNo'),
        ),
    ]