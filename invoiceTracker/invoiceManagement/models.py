from typing import Iterable
from django.db import models


# Create your models here.
class InvoiceHeader(models.Model):
    """
    InvoiceHeader model
    """

    id = models.UUIDField(primary_key=True, max_length=8)
    datetime = models.DateTimeField(auto_now_add=True)
    invoice_number = models.IntegerField(unique=True)
    customer_name = models.CharField(max_length=50)
    billing_address = models.CharField(max_length=100)
    shipping_address = models.CharField(max_length=100)
    gstin = models.CharField(max_length=20)
    total_amount = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self) -> str:
        return super().__str__()

    def save(self, *args, **kwargs):
        self.invoice_number = self.invoice_number + 1
        return super().save(*args, **kwargs)


class InvoiceItems(models.Model):
    """
    InvoiceItems model
    """

    id = models.UUIDField(primary_key=True, max_length=8)
    item_name = models.CharField(max_length=50)
    quantity = models.DecimalField(max_digits=7, decimal_places=2)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    amount = models.DecimalField(max_digits=7, decimal_places=2)
    invoice_header = models.ForeignKey(InvoiceHeader, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return super().__str__()

    def save(self, *args, **kwargs):
        self.amount = self.quantity * self.price
        return super().save(*args, **kwargs)


class InvoiceBillSundry(models.Model):
    """
    InvoiceBillSundry model
    """

    id = models.UUIDField(primary_key=True, max_length=8)
    billsundry = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=7, decimal_places=2)
    invoice_header = models.ForeignKey(InvoiceHeader, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return super().__str__()
