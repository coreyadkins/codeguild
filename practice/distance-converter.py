""""Converts distances between unit types"""
#1. Setup
MI_TO_M = 1609.34
KM_TO_M = 1000
FT_TO_M = 0.3048


#2. Input
starting_unit = input('Hello. I am a program that converts distances. What is' +
                      'your starting unit of measurement?' +
                      ' Please input; mi, km, ft or m. ')

distance_in_starting_unit = float(input('What is your distance amount? '))

output_unit = input('What is your end unit, please input; mi, km, ft or m ? ')

#3. Transform to Meters

if starting_unit == 'mi':
    distance_in_converted_unit = MI_TO_M * distance_in_starting_unit
if starting_unit == 'km':
    distance_in_converted_unit = KM_TO_M * distance_in_starting_unit
if starting_unit == 'ft':
    distance_in_converted_unit = FT_TO_M * distance_in_starting_unit
if starting_unit == 'm':
    distance_in_converted_unit = distance_in_starting_unit

#3b. Transform to Output
if output_unit == 'm':
    distance_in_output_unit = distance_in_converted_unit
if output_unit == 'mi':
    distance_in_output_unit = distance_in_converted_unit / float(MI_TO_M)
if output_unit == 'km':
    distance_in_output_unit = distance_in_converted_unit / KM_TO_M
if output_unit == 'ft':
    distance_in_output_unit = distance_in_converted_unit / FT_TO_M


#4. Output

print('Output: ' + str(distance_in_output_unit))
