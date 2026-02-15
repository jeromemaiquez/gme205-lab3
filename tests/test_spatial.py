from spatial import Point

# Testing refactoring of Point
p = Point("A", 121.0, 14.6)
print(p.id, p.geometry.x, p.geometry.y)
print(p.to_tuple())

q = Point("B", 122.0, 15.6)
print(p.distance_to(q))

# Testing inheritance from SpatialObject to Point
print("BBox: ", p.bbox())
print("Tuple: ", p.to_tuple())

# Testing inheritance from SpatialObject to Parcel
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

print("Parcel BBox: ", parcel.bbox())
print("Parcel Zone: ", parcel.attributes["zone"])

# Testing SpatialObject.intersects()
row_inside = {
    "id": "A",
    "lon": 1.0,
    "lat": 1.6,
    "name": "Inside",
    "tag": "POI"
}

inside = Point.from_dict(row_inside)

row_outside = {
    "id": "B",
    "lon": 121.0,
    "lat": 14.6,
    "name": "Outside",
    "tag": "POI"
}

outside = Point.from_dict(row_outside)

print("Point inside Parcel: ", inside.intersects(parcel))
print("Point outside Parcel: ", outside.intersects(parcel))

# Testing Point.from_dict() and Point.as_dict()
row = {
    "id": "A",
    "lon": 121.0,
    "lat": 14.6,
    "name": "Gate",
    "tag": "POI"
}

p = Point.from_dict(row)
print(p.id, p.to_tuple(), p.name, p.tag)
print(p.as_dict())

invalid_row = {
    "id": "B",
    "lon": 999.0,
    "lat": 14.6,
    "name": "Invalid",
    "tag": "POI"
}

# q = Point.from_dict(invalid_row)