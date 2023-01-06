from .models import Student, Path
from faker import Faker

def run():
    fake = Faker(['tr-TR'])
    paths = (
        'Fullstack',
        'Datascience',
        'AwsDeveps',
        'Cvberces',
    )

    for path in paths:
        new_path = Path.objects.create(path_name = path)
        for _ in range(10):
            Student.objects.create(path = new_path, first_name = fake.first_name(), last_name = fake.last_name(), number = fake.pyint())
        
    print('Finished')

# To activate the faker page:
# 1- pip install Faker
# 2- pip freeze > requirements.txt
# 3- python manage.py shell
# 3.1- from student_api.faker import run
# 3.2- run() (We need to see your Finished text after entering it)
# 3.3- exit()