# Generated by Django 3.1.6 on 2021-03-01 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_and_pay', '0003_auto_20210301_0739'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderproduct',
            name='status',
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('order_is_made', 'Заказ оформлен'), ('order_is_paid', 'Заказ оплачен'), ('order_is_fulfilled', 'Заказ выполнен')], default='order_is_made', max_length=200, verbose_name='Статус'),
        ),
    ]
