import csv
from django.core.management.base import BaseCommand
from parts.models import Part

class Command(BaseCommand):
    help = 'Load parts data from CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='The path to the CSV file')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']
        with open(csv_file, newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                Part.objects.create(
                    category_code=row['category_code'],
                    part_code=row['part_code'],
                    part_name=row['part_name'],
                    part_price=row['part_price']
                )
        self.stdout.write(self.style.SUCCESS('Successfully loaded parts data'))