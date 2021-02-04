import unittest
from testing_your_code import get_formatted_name

class NameTestCasr(unittest.TestCase):
    """will check to see if the function works for first and last name"""

    def test_first_last_name(self):
        """Do simple two word names work like: Tiara Harris"""
        formatted_name = get_formatted_name('tiara', 'harris')
        self.assertEqual(formatted_name, 'Tiara Harris')


    def test_first_middle_last_name(self):
        """will test if names 'the great gasby' work """

        formatted_name = get_formatted_name(
            'the', 'gatsby', 'great')
        self.assertEqual(formatted_name, 'The Great Gatsby')
# this syntax is insane you need to memorize new syntax format 
unittest.main()
# there are programs to create code and to test code do we need people

