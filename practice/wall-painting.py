"""This program will determine the cost of painting a wall"""
#1. Setup
GALLON_COVERAGE = 400 #coverage in Sq. Feet
JOB_COST = 0
AREA_LIST = [0]
SUM_AREA = 0


#2. Input
print('Hello, how many walls will you be painting:')
num_walls = int(input())

print('Cost of a gallon of paint, in dollars:')
paint_cost = float(input())


while num_walls >= 1: #Need to create additive variable which ouputs list that is totalled in SUM_AREA, rather than using SUM_AREA in while loop
    print('Width of the wall in feet:')
    wall_width = int(input())
    print('Height of the wall in feet:')
    wall_height = int(input())
    print('How many coats would you like to put on your wall:')
    num_coats = int(input())
    area = (wall_height * wall_width) * num_coats #Outputs units in Sq. Feet
    print(area)
    AREA_LIST += str(area)
    num_walls -= 1
    print(AREA_LIST)

#3. Transform

import math


SUM_AREA = sum(AREA_LIST)
SUM_AREA = (wall_width * wall_height) * num_coats
gallons_paint = SUM_AREA / GALLON_COVERAGE
gallons_purchased = math.ceil(gallons_paint)
wall_cost = float(gallons_purchased) * paint_cost
JOB_COST += wall_cost

#4. Output
if JOB_COST <= 1:
    print('This job will cost ' + str(round(JOB_COST)) + ' dollar')
else:
    print('This job will cost ' + str(round(JOB_COST)) + ' dollars')
