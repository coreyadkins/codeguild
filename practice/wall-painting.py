"""This program will determine the cost of painting a wall"""
# 1. Define

import math

def gather_wall_sq_ft():
"""This function gathers the number of walls and the dimensions of those walls from the user, transforms the dimensions
into sq ft, and then outputs a list of the square footage of each wall
"""
    walls_to_paint = int(input('Hello, how many wals will you be painting: '))
    list_of_walls_sq_ft = []
    while walls_to_paint > 0:
        current_wall_width_feet = int(input('Width of wall #' + walls_to_paint[-1]' wall in feet: '))
        current_wall_height_feet = int(input('Height of wall in feet: '))
        num_coats = int(input('How many coats would you like to put on your wall: '))
        current_wall_sq_ft = current_wall_width_feet * current_wall_height_feet
        current_wall_sq_ft_to_paint = current_wall_sq_ft *  num_coats
        list_of_walls_sq_ft = [current_wall_sq_ft_to_paint]
        walls_to_paint -= 1
    return list_of_walls_sq_ft

def generate_total_cost(total_sq_feet_to_paint):
"""This function asks the user for the cost of a gallon of paint, then generates the total cost of painting all walls
from the total sq feet given
"""
    GALLON_PAINT_COVERAGE_IN_SQ_FT = 400
    paint_cost_dollars = float(input('Cost of a gallon of paint, in dollars: '))
    gallons_required = total_sq_feet_to_paint / GALLON_PAINT_COVERAGE_IN_SQ_FT
    gallons_to_purchase = math.ceil(gallons_required)
    total_cost_dollars = float(gallons_to_purchase) * paint_cost_dollars
    return total_cost_dollars

def generate_output_statement(total_cost_dollars):
"""This function generates the output statement of the job cost to print"""
if total_cost_dollars == 1:
    output_statement = ('This job will require ' + str(gallons_to_purchase) + ' gallons of paint and cost '+
                        str(round(total_cost_dollars)) + ' dollar')
else:
    output_statement = ('This job will require ' + str(gallons_to_purchase) + ' gallons of paint and cost ' +
                        str(round(total_cost_dollars)) + ' dollars')
    return output_statement


# 2. Main

def main():
    list_of_walls_sq_ft = gather_wall_sq_ft()
    total_sq_feet_to_paint = sum(list_of_walls_sq_ft)
    total_cost_dollars = generate_total_cost(total_sq_feet_to_paint)
    output_statement = generate_output_statement(total_cost_dollars)
    print(output_statement)
    return output_statement


main()


# 3. Input
# 4. Transform
# 5. Output
