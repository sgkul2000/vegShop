from rest_framework import serializers
from .models import Order,Vegitable, Users
from django.contrib.auth.models import User


class usersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Users

class vegitableSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        ordering=['name']
        model=Vegitable
        fields=('id', 'name', 'price', 'pricePer')

class orderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        ordering=['-id']
        model=Order
        fields=('id', 'items', 'orderDate', 'estimatedDelivery', 'amount')
        extra_kwargs={'vegitables':{'required':False},'estimatedDelivery':{'required':False}}

# auth serializers

class UserSigninSerializer(serializers.Serializer):
    username = serializers.CharField(required = True)
    password = serializers.CharField(required = True)


class UserSerializer(serializers.Serializer):
    username = serializers.CharField(required = True)
    email = serializers.CharField(required = True)
    # firstname = serializers.CharField(required = True)
    # class Meta:
        # model=User
        # fields=