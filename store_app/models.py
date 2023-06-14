from django.db import models

#! many to many relationship
class Promotion(models.Model):
    descriction = models.CharField(max_length=255)
    discount = models.FloatField()

#=======================================#

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    
 
#! one To Many relationship

class Collection (models.Model):
    title = models.CharField(max_length=255)
    featured_product = models.ForeignKey(
        'Product',on_delete=models.SET_NULL,null=True , related_name='+')
    
 
class Product(models.Model):
     title = models.CharField(max_length=255)
     description = models.TextField()
     price= models.DecimalField(max_digits=6 , decimal_places= 2)
     inventory = models.IntegerField()
     last_updated = models.DateTimeField(auto_now=True)
     collection= models.ForeignKey(Collection, on_delete=models.PROTECT)  
      
     promotions = models.ManyToManyField(Promotion)
     


class Customer(models.Model):
    MEMBERSHIP_BRONZE = 'B',
    MEMBERSHIP_SLIVER = 'S',
    MEMBERSHIP_GOLD = 'G',

    MEMBER_CHOICES = [
        (MEMBERSHIP_BRONZE, 'Bronze'),
        (MEMBERSHIP_SLIVER, 'Silver'),
        (MEMBERSHIP_GOLD, 'Gold'),
    ]

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=11)
    birth_date = models.DateField(null=True)
    membership = models.CharField(
        max_length=1, choices=MEMBER_CHOICES, default=MEMBERSHIP_BRONZE)


class Order(models.Model):
    PAYMENT_STATUS_PENDING = 'P'
    PAYMENT_STATUS_COMEPLETE = 'C'
    PAYMENT_STATUS_FAILED = 'F'
    PAYMENT_STATUS_CHOICES = [
        (PAYMENT_STATUS_PENDING, 'Pending'),
        (PAYMENT_STATUS_COMEPLETE, 'Completed'),
        (PAYMENT_STATUS_FAILED, 'Failed'),
    ]

    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(
        max_length=1, choices=PAYMENT_STATUS_CHOICES, default=PAYMENT_STATUS_PENDING)
    
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)

class OrderItem(models.Model):
    order= models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6,decimal_places=2)

#! OneToOne

class Address (models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    customer = models.OneToOneField(
        Customer, on_delete=models.CASCADE, primary_key=True)
    
class Card (models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    
class CardItem(models.Model):
    cart = models.ForeignKey(Card,on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)    
    quantity = models.PositiveSmallIntegerField()
    
