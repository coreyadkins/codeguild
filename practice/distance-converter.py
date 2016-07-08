""""Converts distances between unit types"""
#1. Setup
MI_TO_M = 1609.34
KM_TO_M = 1000
FT_TO_M = 0.3048


#2. Input
starting_unit = input('Hello. I am a program that converts distances. What is' +
                      'your starting unit of measurement?' +
                      ' Please input; mi, km, ft or m. ')

starting_distance = input('What is your distance amount? ')

output_unit = input('What is your end unit, please input; mi, km, ft or m ? ')

#3. Transform to Meters
if starting_unit == 'mi':
    converted_to_meters = MI_TO_M * float(starting_distance)
if starting_unit == 'km':
    converted_to_meters = KM_TO_M * float(starting_distance)
if starting_unit == 'ft':
    converted_to_meters = FT_TO_M * float(starting_distance)
if starting_unit == 'm':
    converted_to_meters = float(starting_distance)

#3b. Transform to Output
if output_unit == 'm':
    output = converted_to_meters
if output_unit == 'mi':
    output = converted_to_meters / float(MI_TO_M)
if output_unit == 'km':
    output = converted_to_meters / KM_TO_M
if output_unit == 'ft':
    output = converted_to_meters / FT_TO_M


#4. Output

print('Output: ' + str(output))
