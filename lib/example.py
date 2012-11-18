#!/usr/bin/env python
# coding: utf-8

# Example of rec
import sys
import requests

from string import join
from rec import Rec

def main():
    rec = Rec()

    twitter = {
        'favorites': 'https://api.twitter.com/1/favorites.json?count=20&screen_name={0}'.format( sys.argv[1] ),
        'search': 'http://search.twitter.com/search.json?q={0}&rpp=2&include_entities=true&result_type=mixed'.format( sys.argv[2] )
    }

    favorites = requests.get( twitter['favorites'] )
    search = requests.get( twitter['search'] )

    fav_list = [ tw['text'] for tw in favorites.json ]
    search_list = [ tw['text'] for tw in search.json['results'] ]

    fav_buffer = rec.stack.buffer( fav_list ); 
    fav_frequency = rec.filter.frequency( fav_buffer.getvalue() )
    fav_buffer.close()

    result = rec.stack.filter(
        fav_frequency,
        search_list
    )
    
    print join( result, '\n' )

if __name__ == '__main__':
    main()

