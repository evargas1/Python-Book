import unittest
from testing_your_code import formatted_city_country

class CityTestCase(unittest.TestCase):
    "Test the workablity of formatted_city_country"

    def test_output_city_country(self):
        """Do layouts like Santigo, Chile work"""
        formatted_name = formatted_city_country('santigo', 'chile')
        self.assertEqual(formatted_name, 'Santigo, Chile')

    def test_city_country_population(self):
        """will check to make sure that the function with a number will pass the test."""
        formatted_name = formatted_city_country('santigo', 'chile', 30000)
        self.assertEqual(formatted_name, 'Santigo, Chile - 30000 people.')
        # both test passed yahh with the two dots!


unittest.main()

# if the test fails it is not the test fault most of the time 
# something is wrong with your code so go back and fix it.
