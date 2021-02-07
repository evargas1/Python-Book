# class AnoymusSurvery():
#     """collect anyomus survey question"""

#     def __init__(self, question):
#         """Intialize main variables"""
#         self.question = question
#         self.responses = []

#     def show_question(self):
#         """will print the question you want"""
#         print(self.question)

#     def save_response(self, new_response):
#         """save the responses entered"""
#         self.responses.append(new_response)

#     def show_results(self):
#         """will print results entered"""
#         for r in self.responses:
#             print( '- ' + r.title())

#     def show_first_lang(self):
#         first_response = self.responses[0]
#         print("Great so your first lang was " + first_response.title())


# # define a qesution and than call the function
# question = "What language did you first learn to speak?"
# my_survey = AnoymusSurvery(question)

# my_survey.show_question()
# print("Enter 'q' at any moment to end program")
# while True:
#     response = input("Language: ")
#     if response == 'q':
#         break
#     else:
#         my_survey.save_response(response)

# # print out all the remaining responses 
# print("\n Thnak you for taking our short survey we appreciate you!")
# my_survey.show_results()
# my_survey.show_first_lang()

class Employee():
    """collect infomation on a working employee at a company"""

    def __init__(self, first_name, last_name, salary):
        """define the main attributes in this program"""
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.increase = 5000
        # defining the attributes lets us access them througout out the program

    def see_all_info(self):
        """prints a clean line of code will all the info"""
        print("Hey, Welcome " + self.first_name.title() + " " + self.last_name.title() + " $" + str(self.salary))

    def you_get_raise(self, pay=''):
        """when called witll give you the option of adding a raise defaulut"""
        if pay:
            self.salary += pay
        else:
            self.salary += self.increase
        print("Hey your new salary is now: $" + str(self.salary)  )

jane = Employee('jane', 'adams', 80000)
jane.see_all_info()
jane.you_get_raise()

    




        