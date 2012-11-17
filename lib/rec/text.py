# coding: utf-8
import nltk 

class Text( object ):
    def search( self, frequency={}, text='' ):
        output = {}

        try:
            if frequency and text:
                text_tokens = nltk.tokenize.word_tokenize( text )

                for k,v in frequency.iteritems():
                    for token in text_tokens:
                        if k in output.keys() and k == token:
                            output[k] += 1
                        elif not k in output.keys() and k == token:
                            output[k] = 1

            return output
        except Exception:
            return output


    
