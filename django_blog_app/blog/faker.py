from .models import Blog, Category
from faker import Faker

def run():
    fake = Faker(['tr-TR'])
    categorys=(
        'Sports',
        'Technology',
        'Literature',
        'Global Warming',
    )

    for category in categorys:
        new_category = Category.objects.create(name = category)
        for _ in range(5):
            Blog.objects.create(category = new_category, title = fake.name(), content = fake.text())

    print('Finished')