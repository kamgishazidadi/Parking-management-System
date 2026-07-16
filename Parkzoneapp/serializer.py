from rest_framework import serializers
from .models import *

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class ParkingLotSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingLot
        fields = '__all__'

class ReservationSerializer(serializers.ModelSerializer):
    customer = serializers.SlugRelatedField(
        queryset = Customer.objects.all(),
        slug_field = 'email'
    )
    parkingLot = serializers.SlugRelatedField(
        queryset = ParkingLot.objects.all(),
        slug_field = 'slotNumber'
    )
    class Meta:
        model = Reservation
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):
    customer = serializers.SlugRelatedField(
        queryset = Customer.objects.all(),
        slug_field = 'email'
    )
    
    class Meta:
        model = Payment
        fields = '__all__'
        






class CustomerLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()