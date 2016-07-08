"""This program will determine the cost of painting a wall"""
#1. Setup
GALLON_COVERAGE = 400 #coverage in Sq. Feet
JOB_COST = 0
SUM_AREA = 0


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
    SUM_AREA = (wall_width * wall_height) * num_coats #Outputs units in Sq. Feet
    num_walls -= 1

#3. Transform

import math

gallons_paint = SUM_AREA / GALLON_COVERAGE
wall_cost = float(gallons_paint) * paint_cost
JOB_COST += wall_cost
JOB_COST = math.ceil(JOB_COST)

#4. Output
if JOB_COST <= 1:
    print('This job will cost ' + str(JOB_COST) + ' dollar')
else:
    print('This job will cost ' + str(JOB_COST) + ' dollars')
