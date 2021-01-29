class ClassyL():
    """Will show infomation on a cool resturant"""

    def __init__(self, resturant_name, cuisne_type):
        self.resturant_name = resturant_name
        self.cuisne_type = cuisne_type
        self.number_served = 0
       

    def people_served(self, people):
       
        self.number_served += people
            # the plus sign allows you add people served
            # throughout the span of

    def print_people_served(self):
        """will print todtal number of people have been served."""
        print("There are a total of " + str(self.number_served) + " being served right now")

    def increament_people_served(self, total_people):
        self.number_served += total_people
        print("Great today a total of " + str(self.number_served) + " people were served today")

    def describe_rest(self):
        print(self.resturant_name.title() + " cool place to pick!!")
        print(self.cuisne_type.title() + " love them too!!")
        

    def open_resturant(self):
        """Will let you know we are open"""
        print("We are open today at 1" )

