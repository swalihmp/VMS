from rest_framework.routers import DefaultRouter
from .views import *
from django.urls import path
router=DefaultRouter()
router.register('vendor',viewset=VendorView,basename='Vendor')
router.register('purchase',viewset=PurchaseView,basename='Purchase')
urlpatterns=router.urls
