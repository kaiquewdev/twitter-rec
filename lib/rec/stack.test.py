import unittest
import stack 
import filter

class StackTestSuite( unittest.TestCase ):
    def setUp( self ):
        self.case = []

        self.case.append({
            'frequency': filter.frequency(
                'Simple text, boy simple'
            ),
            'stack': [
                'simple recommendation',
                'text from a simple boy'
            ],
            'result': 'text from a simple boy'
        })

    def test_stack_rec_fail( self ):
        self.assertEqual(
            stack.choose(),
            '' 
        )

    def test_stack_rec_recommendation( self ):
        self.assertEqual(
            stack.choose( 
                self.case[0]['frequency'],
                self.case[0]['stack']
            ),
            self.case[0]['result']
        )   

if __name__ == '__main__':
    unittest.main()
