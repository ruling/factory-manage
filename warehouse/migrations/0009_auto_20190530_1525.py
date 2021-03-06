# Generated by Django 2.0 on 2019-05-30 07:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0008_auto_20190528_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producediary',
            name='staff_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='员工'),
        ),
        migrations.AlterField(
            model_name='purchaselist',
            name='buyer_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='采购员'),
        ),
    ]
