import uuid
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class LNMOnline(models.Model):
    CheckoutRequestID = models.CharField(max_length=255,blank=True,null=True)
    MerchantRequestID = models.CharField(max_length=255,blank=True,null=True)
    ResultCode  = models.CharField(max_length=255,blank=True,null=True)
    ResultDesc  = models.CharField(max_length=255,blank=True,null=True)
    MpesaReceiptNumber = models.CharField(max_length=255,blank=True,null=True)
    Amount = models.FloatField(blank=True,null=True)
    Balance = models.CharField(max_length=255,blank=True,null=True)
    TransactionDate = models.DateTimeField(blank=True,null=True)
    PhoneNumber  = models.CharField(max_length=255,blank=True,null=True)

    def __str__(self):
        return f"{self.PhoneNumber} has sent {self.Amount} >> {self.MpesaReceiptNumber}"
        

STATUS = ((1, "Pending"), (0, "Complete"), (0, "Failed"))

class Transaction(models.Model):
    """This model records all the mpesa payment transactions"""
    transaction_no = models.CharField(default=uuid.uuid4, max_length=50, unique=True)
    phone_number = PhoneNumberField(null=False, blank=False)
    checkout_request_id = models.CharField(max_length=200)
    reference = models.CharField(max_length=40, blank=True)
    description = models.TextField(null=True, blank=True)
    amount = models.CharField(max_length=10)
    status = models.CharField(max_length=15, choices=STATUS, default=1)
    receipt_no = models.CharField(max_length=200, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    ip = models.CharField(max_length=200, blank=True, null=True)

    def __unicode__(self):
        return f"{self.transaction_no}"

    class Meta:
        db_table = "transactions_tbl"

