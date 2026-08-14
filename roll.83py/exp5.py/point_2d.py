import math

# Function to calculate distance between two points
def distance(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

# Function to find farthest point from origin
def farthest_point(points):
    return max(points, key=lambda p: distance((0, 0), p))

# Input points
points = []

n = int(input("Enter number of points: "))

for i in range(n):
    x = float(input("Enter x coordinate: "))
    y = float(input("Enter y coordinate: "))
    points.append((x, y))

# Display points
print("Points:", points)

# Distance between two given points
p1 = points[0]
p2 = points[1]
print("Distance between", p1, "and", p2, "=", distance(p1, p2))

# Farthest point from origin
print("Farthest point from origin:", farthest_point(points))