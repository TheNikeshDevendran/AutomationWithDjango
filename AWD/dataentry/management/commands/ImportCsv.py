from django.core.management.base import BaseCommand,CommandError
import csv
from django.apps import apps
from dataentry.models import Students
class Command(BaseCommand):
    def add_arguments(self,parser):
        parser.add_argument('file_path',type=str,help="CSV file path for importing data")
        parser.add_argument('modelname',type=str,help="Table name for inserting the data")

    
    def handle(self,*args,**kwargs):
        file_path=kwargs['file_path']
        modelName=kwargs['modelname'].capitalize()
        model=None
        for app_config in apps.get_app_configs():
            print(app_config)
            try:
                model=apps.get_model(app_config.label,modelName)
                print(apps.get_model(app_config.label,modelName))
                break
            except LookupError:
                continue
        if not model:
            raise CommandError(f"{modelName} not found in the apps")
    
        with open(file_path,'r') as file:
            reader=csv.DictReader(file)
            for row in reader:
                exists=Students.objects.filter(roll_no=row['roll_no']).exists()
                if not exists:
                    model.objects.create(**row)
                    self.stdout.write(self.style.SUCCESS('Data inserted Successfully'))
                else:
                    self.stdout.write(self.style.WARNING(f'Data with rollno{row['roll_no']} already present'))
                