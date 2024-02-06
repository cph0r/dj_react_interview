from math import sin, cos, sqrt, atan2, radians


def find_distance(truck_coordinates, user_coordinates):
    radius = 6373.0
    user_latitude = radians(user_coordinates.get("latitude"))
    user_longitude = radians(user_coordinates.get("longitude"))
    truck_latitude = radians(truck_coordinates.get("latitude"))
    truck_longitude = radians(truck_coordinates.get("longitude"))
    delta_lon = truck_longitude - user_longitude
    delta_lat = truck_latitude - user_latitude
    a = sin(delta_lat / 2) ** 2 + cos(user_latitude) * cos(truck_latitude) * sin(delta_lon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = radius * c
    return distance
