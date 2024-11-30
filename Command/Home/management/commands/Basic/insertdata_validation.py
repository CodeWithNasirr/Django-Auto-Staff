from django.core.management.base import BaseCommand

from Home.models import Student
class Command(BaseCommand):
    def handle(self, *args, **options):
        datas=[{'Name':"Nasir",'Age':20,'roll':45},
              {'Name':"Asir",'Age':30,'roll':4},
              {'Name':"Basir",'Age':40,'roll':42},
              {'Name':"Amnau",'Age':42,'roll':12},
              {'Name':"Faraha",'Age':44,'roll':32},
              {'Name':"frainha",'Age':42,'roll':62},]
        for data in datas:
            roll=data['roll']
            existing_check=Student.objects.filter(roll=roll).exists()
        
            if not existing_check:
                Student.objects.create(roll=data['roll'],name=data['Name'],age=data['Age'])
            else:
                print(f"Roll: {roll} is Existing ")

        self.stdout.write(self.style.SUCCESS('Insert Data Sucessfully '))