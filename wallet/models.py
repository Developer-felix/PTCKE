from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_save,post_save

from users.models import Account

widrawal_procedure = (
    (1,"Daily"),
    (2,"Weekly"),
    (3,"Monthly"),
    (4, None)
)


class Wallet(models.Model):
    user = models.ForeignKey(Account,on_delete=models.CASCADE)
    #these field gets added if a specific time reaches and negates from the account balance field
    withrawable_balance = models.IntegerField(default=0)
    #these is the original system balance for the parent and the child
    account_balance = models.IntegerField(default = 0)# 250
    ammount_to_withdraw = models.IntegerField(default=0)
    widrawal_procedure = models.PositiveSmallIntegerField(choices=widrawal_procedure,blank=True, null=True,default=4)
    withdrawable_settime = models.CharField(max_length=255,null=True,blank=True)
    updated_at = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    account_phone_number = models.CharField(max_length=255,unique=True,null=True) 

    def save(self, *args, **kwargs):
        self.account_phone_number == self.user.phone_number  
        super(Wallet, self).save(*args, **kwargs)
    
    def __str__(self):
        if self.user.first_name == None:
            return f'{self.user.phone_number } - {self.account_balance}'
        else:
            return f'{self.user.first_name} {self.user.last_name} - {self.account_balance}'

    class Meta:
        db_table = "wallets_tbl"
    
    def detail(self):
        return self.user.first_name 

class WithDrawals(models.Model):
    user = models.ForeignKey(Account,on_delete=models.CASCADE)
    ammount = models.IntegerField(default=0)
    status = models.CharField(max_length=255,null=True,blank=True)
    reason = models.CharField(max_length=255,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    updated_at = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} - {self.ammount}'


@receiver(post_save,sender=Account)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        Wallet.objects.create(user=instance)

    