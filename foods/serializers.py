from rest_framework import serializers
from .models import Food,Comment,Reserveation


class Foodserializer(serializers.ModelSerializer):
    class Meta:
        model=Food
        fields=['name','rate','price','time','photo','type_food','likes','dislikes',]

class Commentserializer(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields=['id','name','email','messege','date',]



class Reserveationserializer(serializers.ModelSerializer):
    class Meta:
        model=Reserveation
        fields=['title','name','email','phone','number','date','time','type_food','number_student',]