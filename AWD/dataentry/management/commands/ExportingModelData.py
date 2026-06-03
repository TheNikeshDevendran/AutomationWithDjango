from django.core.management.base import BaseCommand
# from dataentry.models import Students
import datetime
import csv
from django.apps import apps
class Command(BaseCommand):
   

    def add_arguments(self, parser):
        parser.add_argument('modelname',type=str,help='Model/Tabel name is required for exporting the data')
    def handle(self, *args, **kwargs):
        model_name=kwargs['modelname'].capitalize()
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        file_path=f"exported_{model_name}_{timestamp}.csv"
        
        model=None
        for appconfig in apps.get_app_configs():
            try:
               model=apps.get_model(appconfig.label,model_name)
               break
            except LookupError:
                pass
        
        if not model:
            self.stdout.write(self.style.ERROR(f'{model_name} not found'))
            return 
        data=model.objects.all()
        with open(file_path,'w',newline='') as file:
            CSVwriter=csv.writer(file)
            # it will give us the column name/headers
            CSVwriter.writerow([field.name for field in model._meta.fields])

            for dt in data:
                CSVwriter.writerow([getattr(dt,field.name) for field in model._meta.fields])
        self.stdout.write(self.style.SUCCESS("Data Exported Sucessfully"))
        