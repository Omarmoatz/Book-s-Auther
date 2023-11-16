"""Django's command-line utility for administrative tasks."""
import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()



import random
from faker import Faker
from book.models import Auther, Book, Review

def create_auther(n):
    faker = Faker()
    for x in range(n):
        Auther.objects.create(
            name = faker.name(),
            biography = faker.text(),
        )
    print(f'{n} auther added')


def create_book(n):
    faker = Faker()
    for x in range(n):
        Book.objects.create(
            auther = Auther.objects.all().order_by('?')[0],
            title = faker.name(),
            price = random.randint(1000,4000),
        )
    print(f'{n} book added')

def create_review(n):
    faker = Faker()
    for x in range(n):
        Review.objects.create(
            book = Book.objects.all().order_by('?')[0],
            reviewer_name = faker.name(),
            content = faker.text(),
            rating = random.randint(1,5),
        )
    print(f'{n} review added')


create_auther(100)
create_book(1000)
create_review(1000)