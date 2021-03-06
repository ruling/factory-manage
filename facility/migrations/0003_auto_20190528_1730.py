# Generated by Django 2.0 on 2019-05-28 09:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('facility', '0002_auto_20190528_1723'),
    ]

    operations = [
        migrations.CreateModel(
            name='Baoxiu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baoxiu_time', models.DateField(auto_now=True, verbose_name='保修时间')),
                ('baoxiu_complementary', models.CharField(max_length=200, verbose_name='保修描述')),
                ('baoxiu_staff_name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='保修人')),
                ('facility_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facility.Facility', verbose_name='设备')),
            ],
        ),
        migrations.RemoveField(
            model_name='repair',
            name='baoxiu_complementary',
        ),
        migrations.RemoveField(
            model_name='repair',
            name='baoxiu_staff_name',
        ),
        migrations.RemoveField(
            model_name='repair',
            name='baoxiu_time',
        ),
        migrations.AlterField(
            model_name='repair',
            name='facility_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facility.Baoxiu', verbose_name='设备'),
        ),
        migrations.AlterField(
            model_name='repair',
            name='repair_staff_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='维修人'),
        ),
    ]
