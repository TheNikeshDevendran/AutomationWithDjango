from django.core.management.base import BaseCommand
from dataentry.models import Students
class Command(BaseCommand):
    help="This is reponsible for Inserting the data in the Student entity"

    def add_arguments(self, parser):
        parser.add_argument('name',type=str)
        parser.add_argument('rollno',type=int)
        parser.add_argument('age',type=int)

    def handle(self,*args,**kwargs):
        name=kwargs['name']
        rollno=kwargs['rollno']
        age=kwargs['age']
        Students.objects.create(name=name,roll_no=rollno,age=age)
        self.stdout.write(self.style.SUCCESS("Successfully Inserted.."))
