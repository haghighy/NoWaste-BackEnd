from decimal import Decimal
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from User.models import Restaurant ,Customer
from User.serializers import MyAuthorSerializer
from .models import *

class RestaurantSerializer(serializers.ModelSerializer):
    # def Menu(self):
    def Menu(self,obj):
        foods = Food.objects.filter(restaurant=obj)
        serializer = FoodSerializer(foods, many=True)
        return serializer.data
    menu = serializers.SerializerMethodField(method_name= 'Menu')  

    class Meta:
        model = Restaurant
        address = serializers.CharField(source = 'address')
        fields = ('number','name','address','restaurant_image','rate','date_of_establishment','description','email','restaurant_image','menu','id')

        extra_kwargs = {
            'menu': {'read_only': True},
            'address': {'required': False},
            'name' : {'required': False},
            'email' : {'read_only': True}
        }
    
    def validate_email(self, new_email):
        user = self.context['request'].user
        if Restaurant.objects.exclude(pk=user.pk).filter(email=new_email).exists():
            raise serializers.ValidationError({"email": "This email is already in use."})
        return new_email


    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance
    


class ChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True,source = 'password')

    class Meta:
        model = Restaurant
        fields = ('old_password', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError({"old_password": "Old password is not correct"})
        return value

    def update(self, instance, validated_data):
        user = self.context['request'].user
        #  user = self.context['request'].user

        if not user.is_authenticated:
            raise serializers.ValidationError({"authorize": "You must be logged in to perform this action."})

        if user.pk != self.instance.pk:
            raise serializers.ValidationError({"authorize": "You dont have permission for this user."})

        instance.set_password(validated_data['password'])
        instance.save()

        return instance


class RestaurantSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['name', 'discount', 'rate', 'date_of_establishment','id']
        lookup_field = 'id'


class FoodSerializer(serializers.ModelSerializer):
    class Meta :
        model = Food
        # fields = '__all__'
        fields = '__all__'

class SimpleFoodSerializer(serializers.ModelSerializer):
    class Meta : 
        model = Food
        fields = 'name'

class OrderItemSerializer(serializers.ModelSerializer):
    food_name = SimpleFoodSerializer

    class Meta : 
        model = OrderItem
        fields = ('quantity','food_name')

class GetOrderSerializer(serializers.ModelSerializer):

    def get_total_price(self, order):
        return sum([item.quantity * item.food.price for item in order.orderItems.all()])
    
    def get_discount(self,order:Order):
        return order.restaurant.discount
    
    items = OrderItemSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField()
    discount = serializers.SerializerMethodField()

    class Meta : 
        model = Order
        fields = ('items','total_price','discount')

        extra_kwargs = {
        'items': {'read_only': True},
        'discount': {'read_only': True},
        'total_price': {'read_only': True}
        }
