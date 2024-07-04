import csv
from django.core.management.base import BaseCommand
from parts.models import Part

class Command(BaseCommand):
    help = 'Load parts data from CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='The path to the CSV file')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']

        try:
            with open(csv_file, mode='r', encoding='cp1252') as file:
                reader = csv.DictReader(file)
                #Part.objects.all().delete()  # 기존 데이터 삭제

                for row in reader:
                    Part.objects.create(
                        category_code=row['category_code'],
                        part_code=row['part_code'],
                        part_name=row['part_name'],
                        part_price=row['part_price']
                    )
                self.stdout.write(self.style.SUCCESS('Successfully loaded parts data'))
        except OSError:
            self.stderr.write(self.style.ERROR('File "%s" does not exist or cannot be read' % csv_file))
        except KeyError as e:
            self.stderr.write(self.style.ERROR('Missing column in CSV file: %s' % e))
        except Exception as e:
            self.stderr.write(self.style.ERROR('Error loading parts: %s' % e))