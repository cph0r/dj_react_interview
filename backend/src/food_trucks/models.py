from django.db import models


class FoodTrucks(models.Model):
    location_id = models.IntegerField()
    applicant = models.CharField(max_length=200)
    facility_type = models.CharField(max_length=200)
    location_description = models.TextField()
    address = models.TextField()
    food_items = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return str(self.applicant)
