from products.models import Product
from faker import Faker

def run1():

    '''
    python manage.py shell
    from faker1 import run1
    run1()
    exit()
    '''

    faker = Faker()

    for i in range(1,200):
        product = Product(name=faker.name(), description=faker.paragraph(), is_in_stock=False)
        product.save()

    print('OK')


