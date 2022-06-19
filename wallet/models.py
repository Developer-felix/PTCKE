from datetime import datetime
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

def generate_timestamp():
    unformated_time = datetime.now()
    formated_time = unformated_time.strftime("%Y%m%d%H%M%S")
    return formated_time

#Logic to update the balance of the wallet after 24 hours and weekly and monthly when the time is reached money should move from the wallet_balance to the withrawable_balance field according to the withdrawal_procedure and the withdrawable_settime and the ammount_to_withdraw field
def update_wallet_balance(user_id):
    wallet = Wallet.objects.get(user_id=user_id)
    set_time_s = wallet.updated_at.strftime("%S")
    print(set_time_s)
    set_time_m = wallet.updated_at.strftime("%M")
    print(set_time_m)
    set_time_h = wallet.updated_at.strftime("%H")
    print(set_time_h)
    set_time_d = wallet.updated_at.strftime("%d")
    print(set_time_d)
    set_time_m = wallet.updated_at.strftime("%m")
    print(set_time_m)
    set_time_y = wallet.updated_at.strftime("%Y")
    print(set_time_y)

    curent_time_s = datetime.now().strftime("%S")
    print(curent_time_s)
    curent_time_m = datetime.now().strftime("%M")
    print(curent_time_m)
    curent_time_h = datetime.now().strftime("%H")
    print(curent_time_h)
    curent_time_d = datetime.now().strftime("%d")
    print(curent_time_d)
    curent_time_m = datetime.now().strftime("%m")
    print(curent_time_m)
    curent_time_y = datetime.now().strftime("%Y")
    print(curent_time_y)

    day_difference = int(curent_time_d) - int(set_time_d)
    print("Days : {}",day_difference)
    month_difference = int(curent_time_m) - int(set_time_m)
    print("Month : {}",month_difference)
    year_difference = int(curent_time_y) - int(set_time_y)
    print("Year : {}",year_difference)  
    hour_difference = int(curent_time_h) - (int(set_time_h)+3)
    print("Hours : {}",hour_difference)
    minute_difference = int(curent_time_m) - int(set_time_m)
    print("Minutes : {}",minute_difference)
    second_difference = int(curent_time_s) - int(set_time_s)
    print("Seconds : {}",second_difference)

    #Append Outputs in the format Year-Month-Day-Hour-Minute-Second

    

    set_time = wallet.updated_at.strftime("%Y%m%d%H%M%S")
    print("Set Time",set_time)
    current_time = datetime.now().strftime("%Y%m%d%H%M%S")
    print("Current Time",current_time)
    if wallet.widrawal_procedure == 1:
        #after 24 hours the balance should be moved to the withrawable_balance field and the account_balance field should be updated
        if day_difference == 1:
            wallet.withrawable_balance = wallet.withrawable_balance + wallet.ammount_to_withdraw
            wallet.account_balance = wallet.account_balance - wallet.ammount_to_withdraw
            wallet.updated_at = datetime.now()
            wallet.save()
    elif wallet.widrawal_procedure == 2:
        #after a week the balance should be moved to the withrawable_balance field and the account_balance field should be updated
        if day_difference == 7:
            wallet.withrawable_balance = wallet.withrawable_balance + wallet.ammount_to_withdraw
            wallet.account_balance = wallet.account_balance - wallet.ammount_to_withdraw
            wallet.updated_at = datetime.now()
            wallet.save()

    elif wallet.widrawal_procedure == 3:
        #after a month the balance should be moved to the withrawable_balance field and the account_balance field should be updated
        if day_difference == 30:
            wallet.withrawable_balance = wallet.withrawable_balance + wallet.ammount_to_withdraw
            wallet.account_balance = wallet.account_balance - wallet.ammount_to_withdraw
            wallet.updated_at = datetime.now()
            wallet.save()
    else:
        pass


@receiver(post_save,sender=Account)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        Wallet.objects.create(user=instance)

    