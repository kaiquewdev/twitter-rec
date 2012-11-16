# coding: utf-8
import filter
import text

def choose( frequency={}, stack=[] ):
    output = '' 
    freq_list = []

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
