# coding: utf-8
# Example of rec

import rec
import requests
from string import join

def main():
    favorites_url = 'https://api.twitter.com/1/favorites.json?count=10&screen_name=japaloc'
    favorites = requests.get( favorites_url )
    fav_list = [tw['text'] for tw in favorites.json]
    fav_text = join( fav_list, '\n' )

    fav_frequency = rec.filter.frequency( fav_text )

    search_url = 'http://search.twitter.com/search.json?q=tech&rpp=2&include_entities=true&result_type=mixed'
    search = requests.get( search_url )
    search_list = [ tw['text'] for tw in search.json['results'] ]

    feed_list = search_list[:2]
    
    print rec.stack.choose( fav_frequency, feed_list )

if __name__ == '__main__':
    main()

