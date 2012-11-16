# coding: utf-8
import nltk

def frequency( text='' ):
    output = {} 

    try:
        if text:
            tokens = nltk.tokenize.word_tokenize( text )
            frequency = dict( nltk.FreqDist( tokens ) )
            frequency_values = frequency.values()
            # sort frequency values
            frequency_values.sort()
            # revert sequence
            frequency_values = frequency_values[::-1]

            for k,v in frequency.iteritems():
                for value in frequency_values:
                    if v == value:
                        output[k] = value

        return output
    except Exception:
        return output
