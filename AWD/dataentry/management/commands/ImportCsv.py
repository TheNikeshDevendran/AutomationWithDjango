from django.core.management.base import BaseCommand
import csv
from dataentry.models import Students
class Command(BaseCommand):
    def add_arguments(self,parser):
        help="This will import CSV file data and insert it in the Student Table"
        parser.add_argument('file_path',type=str,help="CSV file path for importing data")
    
    def handle(self,*args,**kwargs):
        file_path=kwargs['file_path']
        with open(file_path,'r') as file:
            reader=csv.DictReader(file)
            for row in reader:
                exists=Students.objects.filter(roll_no=row['roll_no']).exists()
                if not exists:
                    Students.objects.create(**row)
                    self.stdout.write(self.style.SUCCESS('Data inserted Successfully'))
                else:
                    self.stdout.write(self.style.WARNING(f'Data with rollno{row['roll_no']} already present'))
                