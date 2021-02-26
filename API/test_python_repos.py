import unittest
from python_repos import get_status_code, get_the_url

class PythonReposTest(unittest.TestCase):
    """will check to see if the function works for first and last name"""

    # def test_get_the_url(self):
    #     """test to see if the url can be retirved and turned to json format"""
        # formatted_name = get_the_url('https://api.github.com/search/repositories?q=language:javascript&sort=stars')
        # self.assertEqual(formatted_name, (<Response[200]>))

    def test_get_status_code(self):
        """Do simple two word names work like: Tiara Harris"""
        formatted_name = get_status_code('https://api.github.com/search/repositories?q=language:javascript&sort=stars')
        self.assertEqual(formatted_name, 200)

unittest.main()

