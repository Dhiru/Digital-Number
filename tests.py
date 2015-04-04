import unittest
from generate_number_from_file import *

class TestStories(unittest.TestCase):
    def setUp(self):
        self.input_file_name = 'data'
        self.output_file_name = 'output'

    def test_story1(self):
        print "testing for story1"
        check_list = [[1, 2, 1, 2, 1, 2, 1, 2, 1], [1, 2, 1, 2, 1, 2, 1, 2, 1], [1, 2, 1, 2, 1, 2, 1, 2, 1]]
        self.assertEqual(story1(self.input_file_name), check_list)
        
    def test_identify_number(self):
        print "testing for identify_number"
        number = [' ','_',' ','|','_','|','|','_','|']
        self.assertEqual(identify_number(number), 8)
        
    def test_check_sum(self):
        print "testing for check sum"
        number = [1,2,3,4,5,6,7,8,9]
        self.assertEqual(check_sum(number), True)

    def test_check_sum_fakse(self):
        print "testing for failed check sum"
        number = [1,2,1,2,1,2,1,2,1]
        self.assertEqual(check_sum(number), False)


if __name__ == "__main__":
    unittest.main()
