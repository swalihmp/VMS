from django.db import models
from django.db.models import (CASCADE)
from .choices import *

# Create your models here.



class Vendor(models.Model):
    name = models.CharField(max_length= 200,verbose_name=u'Title',null=True,blank=True) 
    contact_details = models.CharField(max_length= 200,verbose_name=u'Contact',null=True,blank=True) 
    address = models.CharField(max_length= 200,verbose_name=u'Address',null=True,blank=True) 
    vendor_code = models.CharField(max_length= 200,verbose_name=u'Vender Code',null=True,blank=True) 
    on_time_delivery_rate  = models.FloatField(max_length= 10,verbose_name=u'On Time Delivery Rate',null=True,blank=True)
    quality_rating_avg  = models.FloatField(max_length= 10,verbose_name=u'Quality Rating',null=True,blank=True)
    average_response_time = models.FloatField(max_length= 200,verbose_name=u'Average Response Time',null=True,blank=True)
    fulfillment_rate = models.FloatField(max_length= 200,verbose_name=u'Percentage of orders fulfilled successfully',null=True,blank=True)
    
    
    def __str__(self):
        return self.name
    


class PurchaseOrder(models.Model):
    po_number = models.CharField(max_length= 10,verbose_name=u'Purchase Number',unique=True)
    vendor = models.ForeignKey(Vendor,related_name='Vendor', on_delete=CASCADE)
    order_date = models.DateTimeField(verbose_name=u'Order Date',null=True,blank=True)
    delivery_date = models.DateTimeField(verbose_name=u'Delivery Date',null=True,blank=True)
    items = models.CharField(max_length= 200,verbose_name=u'Order Items',null=True,blank=True)
    quantity = models.IntegerField(verbose_name=u'Items Quantity',null=True,blank=True)
    status = models.CharField(max_length= 200,verbose_name=u'Status Of Order',choices=STATUS,null=True,blank=True,default='Placed') 
    quality_rating = models.CharField(max_length= 5,verbose_name=u'Quality Rating',null=True,blank=True)
    issue_date = models.DateTimeField(verbose_name=u'Issue Date',null=True,blank=True)
    acknowledgment_date = models.DateTimeField(verbose_name=u'Acknoledgment Date',null=True,blank=True)
    
    def __str__(self):
        return self.po_number