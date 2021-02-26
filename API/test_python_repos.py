import unittest
from python_repos import get_status_code, get_the_url

class NameTestCasr(unittest.TestCase):
    """will check to see if the function works for first and last name"""

    def test_first_last_name(self):
        """Do simple two word names work like: Tiara Harris"""
        formatted_name = get_formatted_name('tiara', 'harris')
        self.assertEqual(formatted_name, 'Tiara Harris')

