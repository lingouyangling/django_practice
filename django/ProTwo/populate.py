import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProTwo.settings')

import django
django.setup()

import random
from faker import Faker
from AppTwo.models import User

fakegen = Faker()

def populate(n=5):
    for entry in range(n):
        fullname = fakegen.name().split()
        fname = fullname[0]
        lname = fullname[1]
        email = fakegen.email()

        User.objects.get_or_create(fname=fname, lname=lname, email=email)

if __name__ == '__main__':
    print('populating script!')
    populate(20)
    print('populating complete')
