"""
Name: Levi Lowther
Date: 01/23/23

Use built-in functions and 
functions from the math module to apply to the Art domain.

To illustrate the ability to call functions and 
display useful results to the user. 

Use your textbook and the examples in this repo to get ideas.

"""

import math

# define some functions

def get_area_of_lot(length, width):
    """
    Return area of a lot given the length and width of the lot.

    Could this fail?

    """

    # Use a try / except / finally block when something 
    # could go wrong
    try: 
        area = length * width
        return area
    except Exception as ex:
        print(f"Error: {ex}")
        return None


# define more functions here (see instuctions)
def donation_round_up(price):
    """ Round up price for donation to art museum"""
    try:
        price = math.ceil(price)
        return price
    except Exception as ex:
        print(f"Error: {ex}")
        return None    

def art_class_cost(hours):
    """ Cost of an instructor lead class based on hours in class"""
    supplies = 30
    hourly_rate = 50
    try:
        cost = supplies + hourly_rate * hours  
        return cost
    except Exception as ex:
        print(f"Error: {ex}")
        return None    

def sum_of_fundraiser(donation_list):
    """ sum of donations during fundraiser """
    donation_list = [2500,100,750,50,1000]
    try:
        donation_list = math.fsum(donation_list)  
        return donation_list
    except Exception as ex:
        print(f"Error: {ex}")
        return None    





# -------------------------------------------------------------
# Call some functions and execute code!

# This is very standard Python - it means
# "If this module is the one being executed, i.e., the main module"
# (as opposed to being imported by another module)
# Literally: "if this module name == the name of the main module"
if __name__ == "__main__":

    # call your functions here (see instructions)
    print("Explore some functions in the math module")
    print()
    print(f"math.comb(5,1) = {math.comb(5,1)}")
    print(f"math.perm(5,1) = {math.perm(5,1)}")
    print()
    print(f"math.comb(5,3) = {math.comb(5,3)}")
    print(f"math.perm(5,3) = {math.perm(5,3)}")
    print()
    print("Call get_area_of_lot with different arguments")
    print()
    print(f"get_area_of_lot(6,2) = {get_area_of_lot(6,2)}")
    print(f"get_area_of_lot(10,-2) = {get_area_of_lot(10,-2)}")
    print(f"get_area_of_lot(6,2) = {get_area_of_lot('six','two')}")
    print()
    print(f"donation_round_up(25.30) = {donation_round_up(25.30)}")
    print()
    print(f"art_class_cost(3) = {art_class_cost(3)}")
    print()
    print(f"sum_of_fundraiser(2) = {sum_of_fundraiser(2)}")