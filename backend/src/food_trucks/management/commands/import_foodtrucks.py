import csv
from django.core.management.base import BaseCommand

from food_trucks.models import FoodTrucks


class Command(BaseCommand):
    help = 'Import food trucks from CSV file'

    def handle(self, *args, **options):
        csv_file_path = '/Users/chiragphor/Downloads/data.csv'
        with open(csv_file_path, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                FoodTrucks.objects.create(
                    location_id=int(row[0]),
                    applicant=row[1],
                    facility_type=row[2],
                    location_description=row[4],
                    address=row[5],
                    food_items=row[11],
                    latitude=float(row[14]),
                    longitude=float(row[15]),
                )

        self.stdout.write(self.style.SUCCESS('Successfully imported food trucks'))