import ask_city
import math

def ask_units():
    print('Please choose the units according to the letters in parentheses: ')
    ans = ''
    units_keys = ['m', 'km', 'M', 'NM', 'ft']
    units = ['Meters', 'Kilometers', 'Miles', 'Nautical miles',  'Feet']
    mults = [1, 1/1000, 1/1609, 1/1852, 3.28]
    units_dict = dict(zip(units_keys, zip(units,mults)))
    while ans not in units_keys:
        ans = input('1. Meters (m)\n2. Kilometers (km)\n3. Miles (M)\n4. Nautical miles (NM)\n5. Feet (ft): ')
        if ans not in units_keys:
            print('Enter a valid unit.')

    return units_dict[ans]

ask_city.intro()
city_1 = ask_city.find_city('first')
city_2 = ask_city.find_city('second')
lat1, lon1, lat2, lon2 = city_1['lat'], city_1['lng'], city_2['lat'], city_2['lng']

units = ask_units()

phi_1 = lat1 * math.pi/180
phi_2 = lat2 * math.pi/180
delta_phi = (lat2-lat1) * math.pi/180
delta_lambda = (lon2-lon1) * math.pi/180

a = math.sin(delta_phi/2)**2 + math.cos(phi_1) * math.cos(phi_2) * math.sin(delta_lambda/2)**2
c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
d = round(6371000 * c * units[1], 2) # Meters is the default unit

print(f"the distance between {city_1['city_ascii']} and {city_2['city_ascii']} is {d} {units[0]}.")