import csv

from django.test import TestCase
from django.urls import reverse
from ..food_trucks.models import FoodTrucks

class FoodTruckTestCase(TestCase):
    # def setUp(self):
        # FoodTrucks.objects.create(name="Food Truck 1", latitude=40.7128, longitude=-74.0060)
        # FoodTrucks.objects.create(name="Food Truck 2", latitude=34.0522, longitude=-118.2437)

    def test_nearest_food_trucks(self):
        reader = csv.reader('/Users/chiragphor/Downloads/data.csv')
        next(reader)  # Skip the header row

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
        response = self.client.get(reverse('nearest_food_trucks', args=('40.7128', '-74.0060')))
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(len(data), 2)  # Expecting two food trucks

    def test_nearest_food_trucks_custom_radius(self):
        response = self.client.get(reverse('nearest_food_trucks', args=('40.7128', '-74.0060')) + '?radius=200')
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(len(data), 2)

    def test_nearest_food_trucks_no_results(self):
        response = self.client.get(reverse('nearest_food_trucks', args=('0', '0')))
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(len(data), 0)