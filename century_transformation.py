# Transforming an year to century - but so far the century is in roman numerals 

def typing_year():
    while True:
        try:
            year = int(input('Type the year you want to convert to century: '))
            break 

        except ValueError:
            print('You have to type an integer number. Eg: 10, 15, 57...')
    
    return year     

year = typing_year() # Unpacking "year" that is returned in a tuple  

def getting_century():
    division = year/100
    division_str = str(division)
    if division_str.endswith('0'):
        century = division 
        century = round(century) # Rouding to standardize the output 
        print(f'The century is: {century}')
    
    else:
        division_int = year//100
        century = division_int + 1 
        print(f'The century is: {century}')


getting_century()