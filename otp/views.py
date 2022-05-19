import random
import string
from django.shortcuts import render

def random_number_generator(size=10, chars=string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
    