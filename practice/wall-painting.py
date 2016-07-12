"""This program will determine the cost of painting a wall"""
# 1. Setup
import math
list_of_walls_sq_ft = [] #  Why does this need to be here? Ask David
GALLON_PAINT_COVERAGE_IN_SQ_FT = 400

# 2. Input
print('Hello, how many walls will you be painting:')
walls_to_paint = int(input())

print('Cost of a gallon of paint, in dollars:')
paint_cost_dollars = float(input())

for number in range (walls_to_paint):
    print('Width of the wall in feet:')
    wall_width_feet = int(input())
    print('Height of the wall in feet:')
    wall_height_feet = int(input())
    print('How many coats would you like to put on your wall:')
    num_coats = int(input())
    current_wall_physical_sq_ft = (wall_height_feet *
                                   wall_width_feet)
    current_wall_sq_ft_to_paint = (current_wall_physical_sq_ft *
                                   num_coats)
    list_of_walls_sq_ft += [current_wall_sq_ft_to_paint]
    walls_to_paint -= 1

#3. Transform

sum_all_walls_sq_ft = sum(list_of_walls_sq_ft)
gallons_required = (sum_all_walls_sq_ft /
                    GALLON_PAINT_COVERAGE_IN_SQ_FT)
gallons_to_purchase = math.ceil(gallons_required)
total_cost_dollars = float(gallons_to_purchase) * paint_cost_dollars

#4. Output
if total_cost_dollars == 1:
    print('This job will require ' + str(gallons_to_purchase) +
          ' gallons of paint and cost '
          + str(round(total_cost_dollars)) + ' dollar')
else:
    print('This job will require ' + str(gallons_to_purchase) +
          ' gallons of paint and cost '
          + str(round(total_cost_dollars)) + ' dollars')
