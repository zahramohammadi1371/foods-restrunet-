from distutils.command.upload import upload
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


class Food(models.Model):
    FOOD_TYPE=[
        ("breakfast","صبحانه"),
        ("drink","نوشیدنی"),
        ("dinner","شام"),
        ("lunch","ناهار")
    ]
    name=models.CharField(max_length=100)
    description=models.CharField(_("توضیحات"),max_length=100)
    rate=models.IntegerField(_("امتیاز"),max_length=100)
    price=models.CharField(_("قیمت"),max_length=100)
    time=models.IntegerField(_("زمان لازم"))
    published_time=models.DateField(_("تاریخ انتشار"),auto_now_add=True,auto_now=False)
    photo=models.ImageField(upload_to='foods/')
    type_food=models.CharField(_("نوع غذا"),max_length=100,choices=FOOD_TYPE,default="drink")
    likes=models.ManyToManyField(User,related_name="bloglikes",blank=True)
    dislikes=models.ManyToManyField(User,related_name="blogdislikes",blank=True)
    def __str__(self):
        return self.name

class Reserveation(models.Model):
    FOOD_TYPE=[
        ("breakfast","صبحانه"),
        ("drink","نوشیدنی"),
        ("dinner","شام"),
        ("lunch","ناهار")
    ]
    title=models.CharField(_("نام غذا"),max_length=100)
    name=models.CharField(_("نام و نام خانوادگی"),max_length=100)
    email=models.EmailField(_("آدرس الکترونیکی"),max_length=255)
    number_student=models.CharField(_("شماره دانشجویی"),max_length=100)
    phone=models.CharField(_("تلفن"),max_length=100)
    number=models.IntegerField(_("تعداد"))
    date=models.DateField(_("تاریخ"),auto_now_add=False,auto_now=False)
    time=models.DateTimeField(_("ساعت"),auto_now_add=False,auto_now=False)
    type_food=models.CharField(_("نوع غذا"),max_length=100,choices=FOOD_TYPE,default="drink")
    def __str__(self):
        return self.email


class Comment(models.Model):
    food=models.ForeignKey("Food",verbose_name=_("food"),related_name="comment",on_delete=models.CASCADE)
    name=models.CharField(_("نام کاربر"),max_length=100)
    email=models.EmailField(_("آدرس الکترونیکی"),max_length=30)
    messege=models.TextField(_("متن نظر"))
    date=models.DateField(_("تاریخ انتشار"),auto_now_add=True,auto_now=False)

    def __str__(self):
            return self.name