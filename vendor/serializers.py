from rest_framework import serializers
from .models import *

class AddVendorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Vendor
        fields=['name','contact_details','address']
        

class GetIdSerializer(serializers.Serializer):
    pk = serializers.IntegerField(min_value=1,required=True)
    


class VendorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Vendor
        fields = '__all__'
        

class AddPurchaseOrderSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PurchaseOrder
        fields = ['vendor','order_date','items','quantity','issue_date']
        

class PurchaseOrderSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PurchaseOrder
        fields = '__all__'