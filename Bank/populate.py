import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Bank.settings')
import django
django.setup()
from bank_site.models import customers,Transfer
from faker import Faker
from random import randint

f = Faker()

for i in range(20):
    t = customers(name=f.name(),email=f.email(),address=f.address(),balance=randint(10000,1000000))
    t.save()