from django.db import models
from decimal import Decimal
from django.utils import timezone

#Customer Model
class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True,blank=True,null=True)
    phone = models.CharField(max_length=11)
    address = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


#Product Model
class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    def __str__(self):
        return f'{self.name} - {self.price}'

# Invoice Model
class Invoice(models.Model):
    choices = (
        ('Pending', 'Pending'),
        ('Paid', 'Paid'),
    )

    ref_number = models.CharField(max_length=50, unique=True)
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    items = models.JSONField(default=list)
    total = models.DecimalField(max_digits=12, decimal_places=2, default=Decimal('0.00'))
    status = models.CharField(max_length=10, choices=choices, default='Pending')
    created_at = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        if not self.items or len(self.items) == 0:
            raise ValueError("Invoice must have at least one item.")

        if not self.ref_number:
            last_invoice = Invoice.objects.last()
            next_id = (last_invoice.id + 1) if last_invoice else 1
            self.ref_number = f"Invoice{next_id:04d}"

        total_amount = Decimal('0.00')
        for item in self.items:
            price = Decimal(item.get('price', '0'))
            qty = int(item.get('quantity', 0))
            item_total = price * qty
            item['total'] = str(item_total)
            total_amount += item_total

        self.total = total_amount
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Invoice {self.ref_number} ({self.customer.first_name})"




class Transaction(models.Model):
    total_sale = models.DecimalField(max_digits=12, decimal_places=2, default=Decimal('0.00'))
    total_payment = models.DecimalField(max_digits=12, decimal_places=2, default=Decimal('0.00'))
    total_receivable = models.DecimalField(max_digits=12, decimal_places=2, default=Decimal('0.00'))

    def update_totals(self):
        self.total_sale = Invoice.objects.filter(status='Pending').aggregate(models.Sum('total'))['total__sum'] or Decimal('0.00')
        self.total_payment = Invoice.objects.filter(status='Paid').aggregate(models.Sum('total'))['total__sum'] or Decimal('0.00')
        self.total_receivable = self.total_sale + self.total_payment
        self.save()

    def __str__(self):
        return f"Sale: {self.total_sale}, Payment: {self.total_payment}, Receivable: {self.total_receivable}"