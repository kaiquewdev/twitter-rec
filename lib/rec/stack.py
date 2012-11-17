# coding: utf-8

import StringIO

from string import join

from text import Text

class Stack( object ):
    def choose( self, frequency={}, stack=[] ):
        output = '' 
        freq_list = []
        text = Text()

        try:
            if frequency and stack: 
                for txt in stack:
                    result = text.search(
                        frequency,
                        txt
                    )

                    total = sum( result.values() )

                    freq_list.append(
                        total
                    ) 

                flid = freq_list.index(
                    max( 
                        freq_list[0], 
                        freq_list[1]
                    )
                )

                output = stack[ flid ]

            return output
        except Exception:
            return output

    def buffer( self, stack=[] ):
        output = StringIO.StringIO()

        try:
            if stack:
                output.write( join( stack, '\n' ) )

            return output
        except Exception:
            return output
