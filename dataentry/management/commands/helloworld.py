from django.core.management import BaseCommand

class Command(BaseCommand):
    def handle(self, *args, **options):
        help="This will print a Hello World.."
        self.stdout.write("Hello World")