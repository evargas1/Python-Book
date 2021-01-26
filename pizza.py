def listing_all_toppings(size, *toppings):
    """Will print all the toppings added to your pizza and size"""
    print("\nYou have a " + str(size) + " in pizza. These are the current toppings you have added: ")
    for top in toppings:
        print("-  " + top.title())

