"""This program will determine the cost of painting a wall"""
#1. Setup
GALLON_COVERAGE = 400 #coverage in Sq. Feet
JOB_COST = 0
AREA_LIST = []
SUM_ALL_AREAS = 0


#2. Input
print('Hello, how many walls will you be painting:')
num_walls = int(input())

print('Cost of a gallon of paint, in dollars:')
paint_cost = float(input())


while num_walls >= 1: #Need to create additive variable which ouputs list that is totalled in SUM_ALL_AREAS, rather than using SUM_ALL_AREAS in while loop
    print('Width of the wall in feet:')
    wall_width = int(input())
    print('Height of the wall in feet:')
    wall_height = int(input())
    print('How many coats would you like to put on your wall:')
    num_coats = int(input())
    wall_area = (wall_height * wall_width) * num_coats #Outputs units in Sq. Feet
    AREA_LIST += [wall_area]
    num_walls -= 1

#3. Transform

import math


SUM_ALL_AREAS = sum(AREA_LIST)
gallons_required = SUM_ALL_AREAS / GALLON_COVERAGE
gallons_to_purchase = math.ceil(gallons_required)
wall_cost = float(gallons_to_purchase) * paint_cost
JOB_COST += wall_cost

#4. Output
if JOB_COST == 1:
    print('This job will require ' + str(gallons_to_purchase) +
        ' gallons of paint and cost ' + str(round(JOB_COST)) + ' dollar')
else:
    print('This job will require ' + str(gallons_to_purchase) +
        ' gallons of paint and cost ' + str(round(JOB_COST)) + ' dollars')
