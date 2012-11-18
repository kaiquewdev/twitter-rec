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

    def slice( self, stack=[], base=2 ):
        output = []

        try:
            if stack:
                c = base
                block = []

                for sid in range( len( stack ) ):
                    item = stack[ sid ] 
                    block.append( item )
                    c -= 1

                    if c == 0 or sid == ( len( stack ) - 1 ):
                        output.append( block )
                        c = base
                        block = []

            return output
        except Exception:
            return output

    def filter( self, frequency={}, stack=[] ):
        output = []

        try:
            if frequency and stack:
                import pdb; pdb.set_trace()
                stack = self.slice(stack)

                for slot in stack:
                    output.append(
                        self.choose(
                            frequency,
                            slot
                        )
                    )

            return output
        except Exception:
            return output
