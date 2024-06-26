from django.db import models
from accounts.models import UserBankAccount
from .constants import Transaction_Type

# Create your models here.

class Transaction(models.Model):
    account = models.ForeignKey(UserBankAccount, related_name = 'transactions', on_delete = models.CASCADE)
    amount = models.DecimalField(decimal_places=2, max_digits = 15)
    balance_after_transaction = models.DecimalField(decimal_places=2, max_digits = 15)
    transaction_type = models.IntegerField(choices=Transaction_Type, null = True)
    timestamp = models.DateTimeField(auto_now_add=True)
    loan_approve = models.BooleanField(default=False) 
    
    class Meta:
        ordering = ['timestamp'] 