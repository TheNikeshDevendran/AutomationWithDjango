from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help="This will display the greeting command..."

    def add_arguments(self, parser):
        parser.add_argument('name',type=str,help='This Specifies User Name') 


    def handle(self, *args, **kwargs):
        try:
           name=kwargs['name']
           self.stdout.write(self.style.SUCCESS(f"Hi {name}"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(str(e)))