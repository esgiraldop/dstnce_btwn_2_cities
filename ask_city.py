import pandas as pd

def intro():
    print('----------------------------')
    print('-------CITY FINDER----------')
    print('----------------------------')
    print('Welcome to the distance finder between two cities.\Please enter the name of two cities')
    print('We recommend not using special characters. If the program do not return any coincidence,')
    print('it will ask you to enter another city name')

def find_city(string):
    cities_df = pd.read_csv('worldcities.csv') # Database from --> https://simplemaps.com/data/world-cities
    subcities_df = pd.DataFrame()
    while len(subcities_df) == 0:
        city = input(f'Please enter the {string} city: ').capitalize()
        subcities_df = cities_df[['city_ascii', 'lat', 'lng', 'country']][cities_df['city_ascii'] == city]
        if len(subcities_df) == 0:
            # Giving another search with the column "city"
            subcities_df = cities_df[['city_ascii', 'lat', 'lng', 'country']][cities_df['city'] == city]
            if len(subcities_df) == 0:
                print('No city was found. Please try with another name: ')

    if len(subcities_df) == 1:
        selctd_city = subcities_df.iloc[0]
        return selctd_city
    elif len(subcities_df) > 1:
        subcities_df.index = range(1, len(subcities_df) + 1)
        print('More than one city was found. The retrieved cities are: ')
        print(subcities_df[['city_ascii', 'country']])
        print('\n')
        ans = '0'
        idx_str = [str(i) for i in subcities_df['country'].index]
        while ans not in idx_str:
            print('Please enter the number to select between:')
            for values in subcities_df.itertuples():
                print(f'{values.Index}. {values.city_ascii}, {values.country}')
            ans = input(': ')

            if ans not in idx_str:
                print('Please enter a valid option.')

        selctd_city = subcities_df.loc[int(ans)]

        return selctd_city


if __name__ == '__main__':
    ans = find_city('first')
    print('your selected city is: ', ans['city_ascii']+', '+ans['country'])