from django.urls import path, include
from rest_framework import generics

from .views import InvoiceBillSundryAPIView, InvoiceHeaderAPIView, InvoiceItemsAPIView

urlpatterns = [
    path("invoice/", InvoiceHeaderAPIView.as_view(), name="invoice-header"),
    path("invoice-item/", InvoiceItemsAPIView.as_view(), name="invoice-item"),
    path(
        "invoice-billsundry/",
        InvoiceBillSundryAPIView.as_view(),
        name="invoice-billsundry",
    ),
]
