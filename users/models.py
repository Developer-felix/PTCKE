from django.db import models

class Account(models.Model):
    username = models.CharField(max_length=255,blank=True,null=True)
    phone = models.CharField(max_length=255,blank=True,null=True)
    pin = models.CharField(max_length=6,blank=True,null=True)
    country = models.CharField(max_length=6,blank=True,null=True)
    is_parent = models.BooleanField(default=False)
    is_parent = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_super_admin = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.username} - {self.phone}'
    
    class Meta:
        pass
    

