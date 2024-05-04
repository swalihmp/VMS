from rest_framework import viewsets,status
from rest_framework.parsers import JSONParser
from . models import *
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action
from rest_framework.response import Response
from VMS.utils import response_generator
from .serializers import *
import random
import string
from datetime import datetime
from rest_framework.exceptions import ValidationError



DEFAULT_SUCCESS_MSG='Successful'
DELETE_SUCCESS_MSG = 'Deleted'
ERROR_DOES_NOT_EXIST = 'Does not exist'

class VendorView(viewsets.ViewSet):
    parser_classes=[JSONParser]
    
    @swagger_auto_schema(operation_description='add new vendor',
    operation_summary='Add Vendor',
    tags=['Vendor'],
    request_body=AddVendorSerializer
    )      
    @action(methods=['POST'],detail=False)
    def add_vendor(self,request):
        try:
            serializer = AddVendorSerializer(data=request.data)
            
            if serializer.is_valid(raise_exception=True):
                
                name = serializer.validated_data['name']
                first_three_letters = name[:3].upper()  # Convert to uppercase for consistency
                
                # Generate 3 random digits
                random_digits = ''.join(random.choices(string.digits, k=3))
                
                # Concatenate name initials and random digits to form vendor code
                vendor_code = first_three_letters + random_digits
                
                # Check if vendor code already exists, regenerate if needed
                while Vendor.objects.filter(vendor_code=vendor_code).exists():
                    random_digits = ''.join(random.choices(string.digits, k=3))
                    vendor_code = first_three_letters + random_digits
                
                # Add the generated vendor code to the validated data
                validated_data = serializer.validated_data
                validated_data['vendor_code'] = vendor_code
                
                serializer = VendorSerializer(data=validated_data)
                if serializer.is_valid():
                    serializer.save()
                
                    return Response(response_generator(status_code=1,success_msg=DEFAULT_SUCCESS_MSG,status=status.HTTP_200_OK)) 
                else:
                    raise ValidationError("Invalid data provided")
                
            else:
                raise ValidationError("Invalid data provided")

        except Exception as e:
            raise e
            
            
    
    
    
    @swagger_auto_schema(
        operation_description='update vendor with id',
        operation_summary='Update Vendor',
        tags=['Vendor'],
        request_body=AddVendorSerializer
    )
    @action(methods=['PUT'], detail=True)
    def update_vendor(self, request, pk=None):
        try:
            serializer = AddVendorSerializer(data=request.data)
            
            if serializer.is_valid(raise_exception=True):
                instance = Vendor.objects.get(id=pk)
                
                if instance:
                    serializer.update(instance, serializer.validated_data)
                    return Response(response_generator(status_code=1, success_msg=DEFAULT_SUCCESS_MSG, status=status.HTTP_200_OK)) 
                else:
                    return Response(response_generator(status_code=0, error_msg=ERROR_DOES_NOT_EXIST, status=status.HTTP_404_NOT_FOUND))
            
            else:
                # Raise ValidationError if serializer is not valid
                raise ValidationError("Invalid data provided")

        except Exception as e:
            raise e

            
    
    
    @swagger_auto_schema(operation_description='get all vendor',
    operation_summary='get all vendor data',
    tags=['Vendor'],
    )      
    @action(methods=['GET'],detail=False)
    def get_allvendor(self,request):
        try:
            vendor = Vendor.objects.all()
            
            serializer = VendorSerializer(vendor, many=True)
            return Response(response_generator(status_code=1,success_msg=DEFAULT_SUCCESS_MSG,data=serializer.data,status=status.HTTP_200_OK))

        except Exception as e:
            raise e
            
        
    
    @swagger_auto_schema(operation_description='get vendor detail using id',
    operation_summary='get vendor details',
    tags=['Vendor'],
    )      
    @action(methods=['GET'],detail=True)
    def get_vendor_details(self, request, pk=None):
        try:
            serializer_obj = GetIdSerializer(data={'pk':pk})
            if serializer_obj.is_valid(raise_exception=True):
                
                instance = Vendor.objects.get(id=serializer_obj.validated_data.get('pk'))
                
                serializer = VendorSerializer(instance)
                return Response(response_generator(status_code=1,success_msg=DEFAULT_SUCCESS_MSG,data=serializer.data,status=status.HTTP_200_OK))
            
            else:
                # Raise ValidationError if serializer is not valid
                raise ValidationError("Invalid data provided")
        except Vendor.DoesNotExist:
            return Response(response_generator(status_code=0, error_msg=ERROR_DOES_NOT_EXIST, status=status.HTTP_404_NOT_FOUND))
        
        except Exception as e:
            raise e
            
            
    
    
    
    @swagger_auto_schema(operation_description='delete vendor using id',
    operation_summary='delete vendor',
    tags=['Vendor']
    )
    @action(methods=['DELETE'],detail=True)
    def delete_vendor(self, request,pk=None):
        try:
            
            serializer = GetIdSerializer(data={'pk':pk})
            
            if serializer.is_valid(raise_exception=True):
                    
                vendor = Vendor.objects.get(id=serializer.validated_data.get('pk'))
                vendor.delete()
                    
                return Response(response_generator(status_code=1,success_msg=DELETE_SUCCESS_MSG,status=status.HTTP_200_OK))
            else:
                # Raise ValidationError if serializer is not valid
                raise ValidationError("Invalid data provided")
            
        except Vendor.DoesNotExist:
            return Response(response_generator(status_code=0, error_msg=ERROR_DOES_NOT_EXIST, status=status.HTTP_404_NOT_FOUND))
            
        except Exception as e:
            raise e
        
        
class PurchaseView(viewsets.ViewSet):
    parser_classes=[JSONParser]
    
    
    @swagger_auto_schema(operation_description='add new purchase order',
    operation_summary='Add Purchase Order',
    tags=['Purchase Order'],
    request_body=AddPurchaseOrderSerializer
    )      
    @action(methods=['POST'],detail=False)
    def add_purchase_order(self,request):
        try:
            serializer = AddPurchaseOrderSerializer(data=request.data)
            
            if serializer.is_valid(raise_exception=True):
                mutable_data = request.data.copy()
                
                vendor_id = request.data.get('vendor')
                
                vendor = Vendor.objects.get(id=vendor_id)
                
                # Generate 3 random digits
                random_digits = ''.join(random.choices(string.digits, k=5))
                
                # Concatenate name initials and random digits to form vendor code
                po_number = 'VMS' + random_digits
                
                # Check if vendor code already exists, regenerate if needed
                while PurchaseOrder.objects.filter(po_number=po_number).exists():
                    random_digits = ''.join(random.choices(string.digits, k=5))
                    po_number = 'VMS' + random_digits
                
                
                mutable_data['po_number'] = po_number
                mutable_data['vendor_id'] = vendor
                
                print(mutable_data)
                serializer = PurchaseOrderSerializer(data=mutable_data)
                if serializer.is_valid():
                    serializer.save()
                
                    return Response(response_generator(status_code=1,success_msg=DEFAULT_SUCCESS_MSG,status=status.HTTP_200_OK)) 
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                
            else:
                raise ValidationError("Invalid data provided")

        except Exception as e:
            raise e
        
        
    
    @swagger_auto_schema(operation_description='acknowledge purchase order by veendor',
    operation_summary='acknowledge purchase order by vendor',
    tags=['Purchase Order']
    )
    @action(methods=['GET'],detail=True)
    def acknowledge_purchase_order(self,request, pk=None):
        try:
            serializer_obj = GetIdSerializer(data={'pk':pk})
            
            if serializer_obj.is_valid(raise_exception=True):
                order = PurchaseOrder.objects.get(id=pk)
                
                current_date = datetime.now()
                order.acknowledgment_date = current_date
                
                order.save()
                            
                return Response(response_generator(status_code=1,success_msg=DEFAULT_SUCCESS_MSG,status=status.HTTP_200_OK)) 
            else:
                return Response(serializer_obj.errors, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            raise e
        
        
    
    @swagger_auto_schema(operation_description='get all purchase orders',
    operation_summary='get all purchase orders',
    tags=['Purchase Order'],
    )      
    @action(methods=['GET'],detail=False)
    def get_allorders(self,request):
        try:
            orders = PurchaseOrder.objects.all()
            
            serializer = PurchaseOrderSerializer(orders, many=True)
            return Response(response_generator(status_code=1,success_msg=DEFAULT_SUCCESS_MSG,data=serializer.data,status=status.HTTP_200_OK))

        except Exception as e:
            raise e
            
        
    
    @swagger_auto_schema(operation_description='get order detail using id',
    operation_summary='get order details with id',
    tags=['Purchase Order'],
    )      
    @action(methods=['GET'],detail=True)
    def get_order_details(self, request, pk=None):
        try:
            serializer_obj = PurchaseOrderSerializer(data={'pk':pk})
            if serializer_obj.is_valid(raise_exception=True):
                
                instance = PurchaseOrder.objects.get(id=serializer_obj.validated_data.get('pk'))
                
                serializer = PurchaseOrderSerializer(instance)
                return Response(response_generator(status_code=1,success_msg=DEFAULT_SUCCESS_MSG,data=serializer.data,status=status.HTTP_200_OK))
            
            else:
                # Raise ValidationError if serializer is not valid
                raise ValidationError("Invalid data provided")
        except Vendor.DoesNotExist:
            return Response(response_generator(status_code=0, error_msg=ERROR_DOES_NOT_EXIST, status=status.HTTP_404_NOT_FOUND))
        
        except Exception as e:
            raise e
        
        
    
    
    @swagger_auto_schema(operation_description='change status of  purchase order by veendor',
    operation_summary='change status of  purchase order by veendor with id',
    tags=['Purchase Order'],
    request_body=StatusChangeSerializer
    )
    @action(methods=['POST'],detail=True)
    def status_change_purchase_order(self,request, pk=None):
        try:
            serializer_obj = StatusChangeSerializer(data=request.data)
            
            if serializer_obj.is_valid(raise_exception=True):
                order = PurchaseOrder.objects.get(id=pk)
                
                order.status = serializer_obj.validated_data.get('status')
                order.save()
                
                if(order.status == 'Completed') :
                    
                    order.delivery_date = datetime.today().date()
                    
                    order.save()
                    
                    
                    completed_orders_count = PurchaseOrder.objects.filter(
                        vendor=order.vendor,
                        status='Completed',
                        delivery_date__lte=order.expected_delivery_date
                    ).count()

                    # Count total completed POs for the vendor
                    total_completed_orders_count = PurchaseOrder.objects.filter(
                        vendor=order.vendor,
                        status='Completed'
                    ).count()

                    # Calculate the ratio
                    if total_completed_orders_count != 0:
                        ratio = completed_orders_count / total_completed_orders_count
                        
                        vendor_obj = Historical_Performance.objects.get(vendor = order.vendor)
                        vendor_obj.on_time_delivery_rate = ratio
                        vendor_obj.date = datetime.now()
                        vendor_obj.save()
                    
                            
                return Response(response_generator(status_code=1,success_msg=DEFAULT_SUCCESS_MSG,status=status.HTTP_200_OK)) 
            else:
                return Response(serializer_obj.errors, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            raise e