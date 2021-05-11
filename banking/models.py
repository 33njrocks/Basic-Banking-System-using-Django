from django.db import models

# Create your models here.
class Customers(models.Model):
    customer_name = models.CharField(max_length=100)
    customer_email = models.CharField(max_length=100)
    balance = models.FloatField(max_length=None)



class Transfer(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    sender = models.ForeignKey(Customers, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(Customers, on_delete=models.CASCADE, related_name='receiver')
    transaction_amount = models.FloatField()