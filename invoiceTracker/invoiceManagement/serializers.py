from rest_framework import serializers

from .models import InvoiceBillSundry, InvoiceHeader, InvoiceItems


class InvoiceHeaderSerializer(serializers.ModelSerializer):
    """
    InvoiceHeader serializer
    """
    class Meta:
        model = InvoiceHeader
        fields = "__all__"


class InvoiceItemsSerializer(serializers.ModelSerializer):
    """
    InvoiceItems serializer
    """

    class Meta:
        model = InvoiceItems
        fields = "__all__"

    def validate_price(self, data):
        """
        validates the price

        Raises:
            Exception: Price cannot be less than 0 (zero)

        Returns:
            data: json
        """
        if data["price"] < 0:
            raise Exception("Price cannot be less than 0 (zero)")
        return data

    def validate_quantity(self, data):
        """
        validates the quantity

        Raises:
            Exception: Quantity cannot be less than 0 (zero)

        Returns:
            data: json
        """
        if data["quantity"] < 0:
            raise Exception("Quantity cannot be less than 0 (zero)")
        return data


class InvoiceBillSundrySerializer(serializers.ModelSerializer):
    """
    InvoiceBillSundry serializer
    """

    class Meta:
        model = InvoiceBillSundry
        fields = "__all__"
