import os, django, random


os.environ.setdefault("DJANGO_SETTINGS_MODULE","mysite2.settings")
django.setup()


from faker import Faker
from app1.models import person
from django.contrib.auth.models import User
from django.utils import timezone


def create_post(N):
    fake = Faker()
    for i in range(N):
        #id = random.randint(1,4)
        name = fake.name()
        email = fake.email()
        contact = random.randint(1000000000,9999999999)
        person.objects.create(name = name,
        emailid = email,
        contactno = contact,
        )

create_post(10)
print("Success")
