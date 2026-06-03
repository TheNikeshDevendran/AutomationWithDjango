from django.core.management.base import BaseCommand
from dataentry.models import Students
import datetime
import csv
class Command(BaseCommand):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    file_path=f"exportedStudent_{timestamp}.csv"
    def handle(self, *args, **options):
        students=Students.objects.all()
        with open(self.file_path,'w',newline='') as file:
            CSVwriter=csv.writer(file)
            CSVwriter.writerow(['RollNO','Name','Age'])
            for student in students:
                CSVwriter.writerow([student.roll_no,student.name,student.age])
        self.stdout.write(self.style.SUCCESS("Data Exported Sucessfully"))
        