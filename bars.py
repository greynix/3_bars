#!/usr/bin/env python3
import json
import argparse
from math import radians, cos, sin, asin, sqrt


def load_data(path): 
    """Open json file (cp1251)"""
    with open(path, encoding='cp1251') as json_file:
        data = json.load(json_file)
    return data    


def get_biggest_bar(data):
    """Some python magic"""
    return max(data, key=lambda k: k['SeatsCount'])


def get_smallest_bar(data):
    """Some python magic"""
    return min(data, key=lambda k: k['SeatsCount'])


def get_closest_bar(data, longitude, latitude):
    """ Haversine formula """
    lat2 = radians(latitude)
    lon2 = radians(longitude)
    d = None
    for i in range(len(data)):
        lat = radians(float(data[i]['Latitude_WGS84']))
        lon = radians(float(data[i]['Longitude_WGS84']))
        dlon = lon2 - lon 
        dlat = lat2 - lat 
        a = sin(dlat/2)**2 + cos(lat) * cos(lat2) * sin(dlon/2)**2
        c = 2 * asin(sqrt(a)) 
        r = 6371 
        if d is None or c * r < d:
            d = c * r 
            bar = i
        else:
            continue
    return data[bar]   


if __name__ == '__main__':
    parser=argparse.ArgumentParser(description='''Bars info.''')
    subparsers = parser.add_subparsers (dest='command')
    biggest_parser = subparsers.add_parser('biggest', help='find biggest bar')
    smallest_parser = subparsers.add_parser('smallest', help='find smallest bar')
    closest_parser = subparsers.add_parser('closest', help='find closest bar')
    closest_group = closest_parser.add_argument_group (title='find closest bar')
    closest_group.add_argument('latitude', type=float)
    closest_group.add_argument('longitude', type=float)
    parser.add_argument('-json_file', type=str, default='data.json', help='path to file')
    
    N = parser.parse_args()
    
    if N.command == 'biggest':
        print(get_biggest_bar(load_data(N.json_file)))
    elif N.command == 'smallest':
        print(get_smallest_bar(load_data(N.json_file)))
    elif N.command == 'closest':
        print(get_closest_bar(load_data(N.json_file),N.longitude,N.latitude))
    else:
        print(get_biggest_bar(load_data(N.json_file)))
