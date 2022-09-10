# Generated by Django 3.2 on 2022-09-10 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='price',
            field=models.IntegerField(max_length=100, verbose_name='قیمت'),
        ),
        migrations.AlterField(
            model_name='food',
            name='rate',
            field=models.CharField(max_length=100, verbose_name='امتیاز'),
        ),
        migrations.AlterField(
            model_name='reserveation',
            name='name',
            field=models.CharField(max_length=100, verbose_name='نام و نام خانوادگی'),
        ),
    ]
