import pandas as pd

def found_city(string):
    cities_df = pd.read_csv('worldcities.csv')
    city = pd.DataFrame()
    print('----------------------------')
    print('-------CITY FINDER----------')
    print('----------------------------')
    print('Welcome to the distance finder between two cities.\Please enter the name of two cities')
    print('We recommend not using special characters. If the program do not return any coincidence,')
    print('it will ask you to enter another city name')
    while len(city) == 0:
        city = input(f'Please enter the {string} city: ')

        # Search in the dataframe

        if len(city) == 0:
            input('No city was found. Please try with another name: ')


    return city # What if there are multiple coincidences?


def find_dist(city1, city 2):
    pass
    return dist # in kilometers?