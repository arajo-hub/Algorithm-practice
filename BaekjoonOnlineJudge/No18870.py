import sys

n = int(sys.stdin.readline())

points = list(map(int, sys.stdin.readline().split()))

sorted_points = sorted(set(points))

sorted_points = {sorted_points[i]:i for i in range(len(sorted_points))}

print(*[sorted_points[i] for i in points])