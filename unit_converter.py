'''
Unit converter:

Miles and Kilometers
Kilograms and Pounds
Celsius and Fahrenheit

'''

def print_menu():
    print('1. Kilometers to Miles')
    print('2. Miles to Kilometers')
    print('3. Kilograms to Pounds')
    print('4. Pounds to Kilograms')
    print('5. Celsius to Fahrenheit')
    print('6. Fahrenheit to Celsius')

def km_miles():
    km = float(input('Enter distance in kilometers: '))
    miles = km / 1.609

    print('Distance in miles: {0}'.format(miles))

def miles_km():
    miles = float(input('Enter distance in miles: '))
    km = miles * 1.609

    print('Distance in kilometers: {0}'.format(km))

def kg_lbs():
    kg = float(input('Enter weight in kilograms: '))
    lbs = kg * 2.20462

    print('Weight in pounds: {0}'.format(lbs))

def lbs_kg():
    lbs = float(input('Enter weight in pounds: '))
    kg = lbs / 2.20462

    print('Weight in kilograms: {0}'.format(kg))

def cel_fahr():
    cel = float(input('Enter temperature in celsius: '))
    fahr = cel * (9 / 5) + 32

    print('Temperature in fahrenheit: {0}'. format(fahr))

def fahr_cel(): 
    fahr = float(input('Enter temperature in fahrenheit: '))
    cel = (fahr - 32) * (5/9)

    print('Temperature in celsius: {0}'.format(cel))


if __name__ == '__main__':
    print_menu()
    choice = input('Which conversion would you like to do?: ')
    if choice == '1':
        km_miles()
    if choice == '2':
        miles_km()
    
    if choice == '3':
        kg_lbs()
    if choice == '4':
        lbs_kg()
    
    if choice == '5':
        cel_fahr()
    if choice == '6':
        fahr_cel()