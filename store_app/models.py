from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)


class Customer(models.Model):
    MEMBERSHIP_BRONZE='B',
    MEMBERSHIP_SLIVER='S',
    MEMBERSHIP_GOLD='G',
    
    MEMBER_CHOICES = [
        (MEMBERSHIP_BRONZE, 'Bronze'),
        (MEMBERSHIP_SLIVER, 'Silver'),
        (MEMBERSHIP_GOLD,'Gold'),
    ]
    
    first_name=models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=11)
    birth_date = models.DateField(null=True)
    membership = models.CharField(max_length=1 ,choices=MEMBER_CHOICES, default=MEMBERSHIP_BRONZE)
    
class Order(models.Model):
    PAYMENT_STATUS_PENDING = 'P'
    PAYMENT_STATUS_COMEPLETE = 'C'
    PAYMENT_STATUS_FAILED = 'F'
    PAYMENT_STATUS_CHOICES =[
            (PAYMENT_STATUS_PENDING,'Pending'),
            (PAYMENT_STATUS_COMEPLETE,'Completed'),
            (PAYMENT_STATUS_FAILED,'Failed'),
        ]
       
    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status= models.CharField(max_length=1, choices=PAYMENT_STATUS_CHOICES, default=PAYMENT_STATUS_PENDING)