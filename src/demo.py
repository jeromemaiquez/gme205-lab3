from spatial import Point

p = Point("A", 121.0, 14.6)
print(p.id, p.geometry.x, p.geometry.y)
print(p.to_tuple())

q = Point("B", 122.0, 15.6)
print(p.distance_to(q))