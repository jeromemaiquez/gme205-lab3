from spatial import Point

# p = Point("A", 121.0, 14.6)
# print("BBox: ", p.bbox())
# print("Tuple: ", p.to_tuple())

# print(p.id, p.geometry.x, p.geometry.y)
# print(p.to_tuple())

# q = Point("B", 122.0, 15.6)
# print(p.distance_to(q))

from shapely.geometry import Polygon
from spatial import Parcel

# A simple rectangle polygon sample
geom = Polygon([
    (0, 0),
    (10, 0),
    (10, 5),
    (0, 5)
])

# Dictionary for added structure
attrs = {
    "area": 50.0,
    "zone": "Residential",
    "is_active": True
}

parcel = Parcel(parcel_id=101, geometry=geom, attributes=attrs)
print(parcel.as_dict())

# print("Parcel BBox: ", parcel.bbox())
# print("Parcel Zone: ", parcel.attributes["zone"])

row = {
    "id": "A",
    "lon": 121.0,
    "lat": 14.6,
    "name": "Gate",
    "tag": "POI"
}

p = Point.from_dict(row)
# print(p.id, p.to_tuple(), p.name, p.tag)
print(p.as_dict())

invalid_row = {
    "id": "B",
    "lon": 999.0,
    "lat": 14.6,
    "name": "Invalid",
    "tag": "POI"
}

# q = Point.from_dict(invalid_row)