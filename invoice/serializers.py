from rest_framework import serializers
from .models import *

class CustomerSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    email = serializers.EmailField()
    phone = serializers.CharField(max_length=11)
    address = serializers.CharField(max_length=200)

    def create(self, validated_data):
        return Customer.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.address = validated_data.get('address', instance.address)
        instance.save()
        return instance

class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    price = serializers.DecimalField(decimal_places=2, max_digits=10)



class InvoiceSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    ref_number = serializers.CharField(read_only=True)
    customer = serializers.PrimaryKeyRelatedField(queryset=Customer.objects.all())
    items = serializers.ListField(child=serializers.DictField())
    total = serializers.DecimalField(max_digits=12, decimal_places=2, read_only=True)
    status = serializers.ChoiceField(choices=[('Pending','Pending'),('Paid','Paid')], default='Pending')
    created_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        customer = validated_data.get('customer')
        items_data = validated_data.get('items', [])
        if not items_data:
            raise serializers.ValidationError("Invoice must have at least one item.")

        total_amount = Decimal('0.00')
        processed_items = []
        for item in items_data:
            product_id = item.get('product')
            quantity = int(item.get('quantity', 0))

            if not product_id or quantity <= 0:
                raise serializers.ValidationError("Each item must have a valid product and quantity.")

            try:
                product = Product.objects.get(id=product_id)
            except Product.DoesNotExist:
                raise serializers.ValidationError(f"Product with ID {product_id} not found.")

            item_total = product.price * quantity
            total_amount += item_total

            processed_items.append({
                'product': product.id,
                'name': product.name,
                'price': str(product.price),
                'quantity': quantity,
                'total': str(item_total),
            })

        invoice = Invoice.objects.create(
            customer=customer,
            items=processed_items,
            total=total_amount,
            status='Pending'
        )

        return invoice

    def update(self, instance, validated_data):

        status_value = validated_data.get('status', instance.status)


        if status_value == 'Paid' and instance.status != 'Paid':
            instance.status = 'Paid'
            instance.save()
        return instance