from django.core.management.base import BaseCommand
from Home.models import Student
class Command(BaseCommand):
    help = 'Inserts data into the database'

    def handle(self, *args, **options):
        # Add data insertion logic here
        datas=[{'Name':"Nasir",'Age':20,'roll':45},
              {'Name':"Asir",'Age':30,'roll':4},
              {'Name':"Basir",'Age':40,'roll':42}]
        for data in datas:
            Student.objects.create(roll=data['roll'],name=data['Name'],age=data['Age'])

        #For Checking This 
        # for data in datas:
        #     print(f"Name: {data['Name']} Age:{data['Age']} roll: {data['roll']} ")

        self.stdout.write(self.style.SUCCESS('Successfully inserted data'))
