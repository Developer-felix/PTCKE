
import random
import string

from transaction.models import Transaction

def generate_transaction_code_id():
    alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    code = random_number_generator(10, alphabet)
    while Transaction.objects.filter(transaction_id=code).exists():
        code = random_number_generator()

    return f"PTC-{code}"


def random_number_generator(size=10, chars=string.digits):
    return ''.join(random.choice(chars) for _ in range(size))