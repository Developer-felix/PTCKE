from django.test import TestCase
from ..models import Account

class AccountTestCase(TestCase):
    def setUp(self):
        Account.objects.create(
            user_name="Felix", 
            password="onjomba123@",
            phone_number = "254717713943",
            is_parent = True,
            is_child = False
            )
        Account.objects.create(
            user_name="Victor", 
            password="victor123@",
            phone_number = "254798119889",
            is_parent = False,
            is_child = True
            )
    def test_Accounts_can_getfunctionality(self):
        """Accounts get the individuals"""
        lion = Account.objects.get(is_parent=True)
        cat = Account.objects.get(is_child=True)