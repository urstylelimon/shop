from itertools import product

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Customer
from .serializers import *
from django.shortcuts import get_object_or_404


# This is for Customer
@api_view(['POST'])
def create_customer(request):
    serializer = CustomerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET'])
def all_customer(request):
    customers = Customer.objects.all()
    serializer = CustomerSerializer(customers, many=True)
    return Response(serializer.data)
@api_view(['GET','PUT'])
def single_customer(request, pk):
    customer = get_object_or_404(Customer, id=pk)

    if request.method == 'GET':
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CustomerSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def delete_customer(request, pk):
    customer = get_object_or_404(Customer, id=pk)
    customer.delete()
    return Response(status=204)


#This is for Product
@api_view(['GET'])
def product_list(request):
    products = Product.objects.all()

    if not products.exists():
        return Response(
            {"detail": "No products are currently available."},
            status=status.HTTP_404_NOT_FOUND
        )

    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_invoice(request):
    serializer = InvoiceSerializer(data=request.data)
    if serializer.is_valid():
        invoice = serializer.save()
        return Response(InvoiceSerializer(invoice).data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def all_invoice(request):

    invoices = Invoice.objects.all().order_by('-created_at')
    serializer = InvoiceSerializer(invoices, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)