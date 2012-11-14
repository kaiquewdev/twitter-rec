import unittest
import filter

class FilterTestSuite( unittest.TestCase ):
    def setUp( self ):
        self.case = []

        self.case.append({
            'text': 'Hello boy',
            'frequency': {
                'Hello': 1,
                'boy': 1
            }
        })

        self.case.append({
            'text': 'simple command repetition simple buzz buzz buzz',
            'frequency': {
                'buzz': 3,
                'simple': 2,
                'command': 1,
                'repetition': 1,
            }
        })

    def test_filter_frequency_fail( self ):
        self.assertEqual(
            filter.frequency(),
            {}
        )

    def test_filter_frequency_simple( self ):
        self.assertEqual(
            filter.frequency(self.case[0]['text']),
            self.case[0]['frequency']
        )
    
    def test_filter_frequency_ordered( self ):
        self.assertEqual(
            filter.frequency(self.case[1]['text']),
            self.case[1]['frequency']
        )

if __name__ == '__main__':
    unittest.main()
