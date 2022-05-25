import uuid
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from users.models import Account


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
    reciever = models.ForeignKey(Account,on_delete=models.CASCADE,related_name="reciever",blank=True,null=True)
    sender = models.ForeignKey(Account,on_delete=models.CASCADE,related_name="sender",blank=True,null=True)
    user = models.ForeignKey(Account,on_delete=models.CASCADE,related_name="transaction_user",blank=True,null=True)
    transaction_id = models.CharField(max_length=255,blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True,blank=True,null=True)
    ammount = models.IntegerField(default = 0)
    is_withdrawal = models.BooleanField(default=False)
    is_sending = models.BooleanField(default=True)

    # def save(self, *args, **kwargs):
    #     self.transaction_id = generate_transaction_code_id()
    #     super(Transaction, self).save(*args, **kwargs)

    class Meta:
        db_table = "transactions_tbl"

