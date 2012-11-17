# coding: utf-8
# Example of rec

import sys
import rec
import requests
import StringIO

from string import join

def main():
    favorites_url = 'https://api.twitter.com/1/favorites.json?count=10&screen_name={0}'.format( sys.argv[1] )
    favorites = requests.get( favorites_url )

    fav_list = [tw['text'] for tw in favorites.json]
    fav_text = join( fav_list, '\n' )

    fav_buffer = StringIO.StringIO()
    fav_buffer.write( fav_text )

    fav_frequency = rec.filter.frequency( fav_buffer.getvalue() )

    search_url = 'http://search.twitter.com/search.json?q={0}&rpp=2&include_entities=true&result_type=mixed'.format( sys.argv[2] )
    search = requests.get( search_url )
    search_list = [ tw['text'] for tw in search.json['results'] ]

    feed_list = search_list[:2]
    
    fav_buffer.close()
    
    print rec.stack.choose( fav_frequency, feed_list )

if __name__ == '__main__':
    main()

