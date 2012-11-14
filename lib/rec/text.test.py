import unittest
import filter
import text 

class TextTestSuite( unittest.TestCase ):
    def setUp( self ):
        self.case = []

        self.case.append({
            'text': 'hello boy just hello',
            'target': 'simple hello boy',
            'cross': {
                'hello': 1,
                'boy': 1,
            }
        })

    def test_text_search_fail( self ):
        self.assertEqual(
            text.search(),
            {}
        )

    def test_text_search_ocurrencies( self ):
        self.case[0]['frequency'] = filter.frequency(
            self.case[0]['text']
        )

        self.assertEqual(
            text.search(
                self.case[0]['frequency'],
                self.case[0]['target']
            ),
            self.case[0]['cross']
        )
        

if __name__ == '__main__':
    unittest.main()
