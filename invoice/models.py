from django.db import models

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
