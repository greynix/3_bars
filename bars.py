#!/usr/bin/env python3
import json
import argparse
from math import radians, cos, sin, asin, sqrt
import os


def load_data(path): 
    """Open json file (cp1251)"""
    if not os.path.exists(path):
        raise FileNotFoundError('json file not found, please set correct file')   
    with open(path, encoding='cp1251') as json_file:
            return json.load(json_file)

def get_biggest_bar(data):
    """Some python magic"""
    return max(data, key=lambda k: k['SeatsCount'])


def get_smallest_bar(data):
    """Some python magic"""
    return min(data, key=lambda k: k['SeatsCount'])


def get_closest_bar(data, longitude, latitude):
    """ Haversine formula """
    our_latitude = radians(latitude)
    our_longitude = radians(longitude)
    distance = None
    for bar in data:
        bar_latitude = radians(float(bar['Latitude_WGS84']))
        bar_longitude = radians(float(bar['Longitude_WGS84']))
        dist_longitude = our_longitude - bar_longitude
        dist_latitude = our_latitude - bar_latitude 
        a = sin(dist_latitude/2)**2 + cos(bar_latitude) * cos(our_latitude) * sin(dist_longitude/2)**2
        c = 2 * asin(sqrt(a)) 
        earth_radius = 6371 
        if not distance or c * earth_radius < distance:
            distance = c * earth_radius  
            closest_bar = bar
    return closest_bar


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
