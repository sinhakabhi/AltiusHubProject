from django.shortcuts import render
from rest_framework import generics

from .models import InvoiceBillSundry, InvoiceHeader, InvoiceItems
from .serializers import (
    InvoiceBillSundrySerializer,
    InvoiceHeaderSerializer,
    InvoiceItemsSerializer,
)

# Create your views here.


class InvoiceHeaderAPIView(generics.ListAPIView):
    queryset = InvoiceHeader.objects.all()
    serializer_class = InvoiceHeaderSerializer

class InvoiceHeaderAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = InvoiceHeader.objects.all()
    serializer_class = InvoiceHeaderSerializer

class InvoiceHeaderAPIView(generics.CreateAPIView):
    queryset = InvoiceHeader.objects.all()
    serializer_class = InvoiceHeaderSerializer


class InvoiceItemsAPIView(generics.ListAPIView):
    queryset = InvoiceItems.objects.all()
    serializer_class = InvoiceItemsSerializer

class InvoiceItemsAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = InvoiceItems.objects.all()
    serializer_class = InvoiceItemsSerializer

class InvoiceItemsAPIView(generics.CreateAPIView):
    queryset = InvoiceItems.objects.all()
    serializer_class = InvoiceItemsSerializer


class InvoiceBillSundryAPIView(generics.ListAPIView):
    queryset = InvoiceBillSundry.objects.all()
    serializer_class = InvoiceBillSundrySerializer

class InvoiceBillSundryAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = InvoiceBillSundry.objects.all()
    serializer_class = InvoiceBillSundrySerializer

class InvoiceBillSundryAPIView(generics.CreateAPIView):
    queryset = InvoiceBillSundry.objects.all()
    serializer_class = InvoiceBillSundrySerializer
