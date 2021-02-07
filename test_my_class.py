import unittest
from a_class_to_a_test import Employee
# from a_class_to_a_test import AnoymusSurvery


# class TestAnoymusSurvery(unittest.TestCase):
#     """will run test on the class anoymus survery"""

#     def test_store_single_reponse(self):
#         """Test that a single response is stored in a list"""
#         question = "What is the first language you learned to speak?"
#         my_survey = AnoymusSurvery(question)
#         # you can type in any lang and it will save it and the test will pass
#         my_survey.save_response('English')

#         self.assertIn('English', my_survey.responses)
#         # will check if our response of english has been saved

#     def test_three_repsonses(self):
#         """will check to see if 3 responses were saved. Uses assertIn"""
#         question = "What is the first lang you learned?"
#         my_survey = AnoymusSurvery(question)
#         re = ['spanish', 'english', 'french']
#         for r in re:
#             my_survey.save_response(r)
# # it passed all the main test
#         for r in re:
#             self.assertIn(r, my_survey.responses)

        

# unittest.main()


# class TestAnoymusSurvery(unittest.TestCase):
#     """will run any test for the class anoymus survey"""

#     def setUp(self):
#         """Initailze the variables I will need throughout this program"""
#         question = "Hey what is one of the first languages that you learned?"
#         self.my_survey = AnoymusSurvery(question)
#         self.my_response = ['spanish', 'english', 'french']
#         # using the self. prefix allows us to use these instances throughout are program

#     def test_one_response(self):
#         """will test to see if one reponse runs as intended"""
#         self.my_survey.save_response(self.my_response[0])
#         # utlizing the self method again make it look more complicated
#         self.assertIn(self.my_response[0], self.my_survey.responses)
#         # is the first item in my list saved in the responses list?
#         # nothing is saved to a variable

#     def test_three_repsonses(self):
#         """will test to ensure three respones are saved """
#         for res in self.my_response:
#             self.my_survey.save_response(res)
#         for res in self.my_response:
#             self.assertIn(res, self.my_survey.responses)

# unittest.main()

class TestEmployee(unittest.TestCase):
    """This will test the two main function performed within the employee class"""

    # def setUp(self):
    #     # janet = ('janet', 'daniles', 30000)
    #     self.my_person = Employee('janet', 'daniles', 30000)
        

    # def test_name_default_salary(self):
    #     self.my_person.see_all_info()
    #     self.assertEqual('Janet Daniles. You have a current salary of $35000', self.my_person.see_all_info())


    def setUp(self):
    
        self.person = Employee('brad', 'janice', 60000)
        self.increase = (30000)


    def test_give_default_raise(self):
        self.person.you_get_raise(self.increase)
        self.assertIn(self.increase, self.person.increase)
        
        







unittest.main()
        










    


