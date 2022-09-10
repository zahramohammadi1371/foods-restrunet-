# Generated by Django 3.2 on 2022-09-10 18:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserveation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='نام غذا')),
                ('name', models.CharField(max_length=100, verbose_name='نام و نام خانوعوادگی')),
                ('email', models.EmailField(max_length=255, verbose_name='آدرس الکترونیکی')),
                ('number_student', models.CharField(max_length=100, verbose_name='شماره دانشجویی')),
                ('phone', models.CharField(max_length=100, verbose_name='تلفن')),
                ('number', models.IntegerField(verbose_name='تعداد')),
                ('date', models.DateField(verbose_name='تاریخ')),
                ('time', models.DateTimeField(verbose_name='ساعت')),
                ('type_food', models.CharField(choices=[('breakfast', 'صبحانه'), ('drink', 'نوشیدنی'), ('dinner', 'شام'), ('lunch', 'ناهار')], default='drink', max_length=100, verbose_name='نوع غذا')),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100, verbose_name='توضیحات')),
                ('rate', models.IntegerField(verbose_name='امتیاز')),
                ('price', models.IntegerField()),
                ('time', models.DateField(verbose_name='زمان لازم')),
                ('published_time', models.DateField(auto_now_add=True, verbose_name='تاریخ انتشار')),
                ('photo', models.ImageField(upload_to='foods/')),
                ('type_food', models.CharField(choices=[('breakfast', 'صبحانه'), ('drink', 'نوشیدنی'), ('dinner', 'شام'), ('lunch', 'ناهار')], default='drink', max_length=100, verbose_name='نوع غذا')),
                ('dislikes', models.ManyToManyField(blank=True, related_name='blogdislikes', to=settings.AUTH_USER_MODEL)),
                ('likes', models.ManyToManyField(blank=True, related_name='bloglikes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='نام کاربر')),
                ('email', models.EmailField(max_length=30, verbose_name='آدرس الکترونیکی')),
                ('messege', models.TextField(verbose_name='متن نظر')),
                ('date', models.DateField(auto_now_add=True, verbose_name='تاریخ انتشار')),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='foods.food', verbose_name='food')),
            ],
        ),
    ]