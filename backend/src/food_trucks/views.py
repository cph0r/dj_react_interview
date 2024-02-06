from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from food_trucks.models import FoodTrucks
import json

from food_trucks.utils import find_distance


@csrf_exempt
def find_food_trucks(request):
    if request.method == "POST":
        parsed = json.loads(request.body)
        eligible_trucks = []
        radius = parsed['radius']
        user_coordinates = {
            "latitude": parsed['location']['latitude'],
            "longitude":  parsed['location']['longitude']
        }

        food_trucks = FoodTrucks.objects.all().order_by('location_id')

        for truck in food_trucks:
            truck_coordinates = {"latitude":truck.latitude, "longitude":truck.longitude}
            distance = find_distance(user_coordinates, truck_coordinates)
            if distance <= float(radius):
                eligible_trucks.append({'name': truck.applicant, 'address': truck.address, 'menu': truck.food_items, "distance": distance})

        return JsonResponse(eligible_trucks, safe=False)
