import unittest
from stack import Stack
from filter import Filter

stack = Stack()
filter = Filter()

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

    def test_stack_of_text_buffer( self ):
        import StringIO
        from string import join

        assertion_buffer = StringIO.StringIO()
        assertion_buffer.write( 
            join(
                self.case[0],
                '\n'
            ) 
        )
        
        self.assertEqual(
            stack.buffer(
                self.case[0]['stack']
            ).__module__,
            'StringIO' 
        )

        self.assertEqual(
            str(
                type(
                    stack.buffer(
                        self.case[0]['stack']
                    )
                )
            ),
            '<type \'instance\'>' 
        )

        assertion_buffer.close()

    def test_stack_slice( self ):
        self.assertEqual(
            stack.slice([
                '#number1',
                '#number2',
                '#number3',
                '#number4',
            ]), [
                ['#number1', '#number2'],
                ['#number3', '#number4'],
            ]
        )

        self.assertEqual(
            stack.slice([
                '#number1',
                '#number2',
                '#number3',
            ]), [
                ['#number1', '#number2'],
                ['#number3'],
            ]
        )

if __name__ == '__main__':
    unittest.main()
