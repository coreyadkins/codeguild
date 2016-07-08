"""This program will determine the cost of painting a wall"""
#1. Setup
GALLON_COVERAGE = 400 #coverage in Sq. Feet
job_cost = 0


#2. Input
print('Hello, how many walls will you be painting:')
num_walls = int(input())

print('Cost of a gallon of paint, in dollars:')
paint_cost = float(input())


while num_walls >= 1:
    print('Width of the wall in feet:')
    wall_width = int(input())
    print('Height of the wall in feet:')
    wall_height = int(input())
    print('How many coats would you like to put on your wall:')
    num_coats = int(input())
    wall_area = wall_width * wall_height
    gallons_paint = wall_area / GALLON_COVERAGE
    gallons_paint *= num_coats
    wall_cost = float(gallons_paint) * paint_cost
    job_cost += wall_cost
    num_walls -= 1

#3. Transform

import math

job_cost = math.ceil(job_cost)

#4. Output
if job_cost <= 1:
    print('This job will cost ' + str(job_cost) + ' dollar')
else:
    print('This job will cost ' + str(job_cost) + ' dollars')
