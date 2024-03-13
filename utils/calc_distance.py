from math import radians, sin, cos, sqrt, atan2

def calculate_distance(coord1, coord2):
    earth_radius = 6371.0

    lat1 = radians(coord1[0])
    lon1 = radians(coord1[1])
    lat2 = radians(coord2[0])
    lon2 = radians(coord2[1])

    d_lon = lon2 - lon1
    d_lat = lat2 - lat1

    a = sin(d_lat / 2)**2 + cos(lat1) * cos(lat2) * sin(d_lon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = earth_radius * c

    return distance
