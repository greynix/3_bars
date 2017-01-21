import json
import argparse
from math import sqrt
import os


def load_data(path): 
    with open(path, encoding='cp1251') as json_file:
        return json.load(json_file)

def get_biggest_bar(data):
    """
    We find a bar with a maximum places.

    This can be written as :
    def some_function(each_bar):
        return each_bar['SeatsCount']
    return max(data, key=some_function)
    """

    return max(data, key=lambda k: k['SeatsCount'])


def get_smallest_bar(data):
    """
    We find a bar with a minimum places.

    This can be written as :
    def some_function(each_bar):
        return each_bar['SeatsCount']
    return min(data, key=some_function)
    """

    return min(data, key=lambda k: k['SeatsCount'])


def get_closest_bar(data, longitude, latitude):
    """
    We find the nearest bar using Euclidian algorithm 
    
    Distance=sqrt((x1 - x2)**2 + (y1 - y2)**2), where:
    x1 - longitude first bar
    x1 - longitude second bar
    y1 - latitude first bar
    y2 - latitude second bar
    sqrt - square root 
    """

    return min(data, key=lambda bar: \
    sqrt((float(bar['Longitude_WGS84']) - float(longitude))**2 +\
    (float(bar['Latitude_WGS84']) - float(latitude))**2))


if __name__ == '__main__':
    parser=argparse.ArgumentParser(description='''Bars info.''')
    parser.add_argument('json_file', type=str, default='data.json', help='path to file')
    subparsers = parser.add_subparsers (dest='command')
    biggest_parser = subparsers.add_parser('biggest', help='find biggest bar')
    smallest_parser = subparsers.add_parser('smallest', help='find smallest bar')
    closest_parser = subparsers.add_parser('closest', help='find closest bar')
    closest_group = closest_parser.add_argument_group (title='find closest bar')
    closest_group.add_argument('latitude', type=float)
    closest_group.add_argument('longitude', type=float)
    
    user_input = parser.parse_args()
    
    if user_input.command == 'biggest':
         print(get_biggest_bar(load_data(user_input.json_file)))
    elif user_input.command == 'smallest':
        print(get_smallest_bar(load_data(user_input.json_file)))
    elif user_input.command == 'closest':
        print(get_closest_bar(load_data(user_input.json_file),user_input.longitude,user_input.latitude))
    else:
        print(get_biggest_bar(load_data(user_input.json_file)))
