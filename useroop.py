"""
Build a PyBuddy to illustrate Python skills.

Overview:

Name: Levi Lowther
Date:01/24/23

To add some code and call some stats functiontions and have some fun with my domain. 

This example introduces a common way to organize code - into
classes that reflect the real world.

Each class is a combination of attributes (data)
and methods (functions) that operate on that data.

Look for the nouns in your application. 
For example, if you want to code a poker game, you'd make classes for:

- Card, Deck, Hand, Player, Game, etc.

You then use the Card class to create 52 instances of cards,
each with a number/rank and suit, 
e.g. an instance/object to represent the Jack of Spades.

Object-Oriented Programming in Python

- Python allows you to create classes - or data classes
- You don't have to organize your code this way
- Implement classes where you'll instantiate one or more with 
  specific data. Do want makes sense.

We'll use it here, because we want to instantiate 
several PyBuddies, each with different attributes, 
but sharing common behaviors (methods).

A method is a function that is part of a class.

When instantating a PyBuddy, you can create 
a DOG, a CAT, an ELF, or other type.

Python Organization:

Unlike other languages, 
Python does not always have just one class per file.
In this file, we have our enumerated class for the species, 
as well as the main PyBuddy class.

This example:

- uses an object-oriented approach
- wraps functionality into a named class
- the class can be instantiated many times
- (e.g. a cat named Boots, a dog named Rex)
- classes define:
    - properties (class data)
    - methods (class functions)

All Python classes need a built-in class method called __init__:
__init__ is used to create an instance of this class

Python includes an implicit pointer to the instance as a whole
By convention, 
most analysts name this first implicit parameter 'self'
You can change it, but violating customs is considered bad form.
"""

# first, import helpful modules to make our job easier

import datetime
import statistics as stats
from enum import Enum


class Species(Enum):
    DOG = 1
    CAT = 2
    ELF = 3
    ORC = 4
    ARTIST = 5


class PyBuddy:
    """ PyBuddy class for creating a study buddy."""

    def __init__(self, name, species, num_legs, num_ears, weight_kgs, num_works_art, is_available, skill_list, previous_donations):
        """ Built-in method to create a new instance."""
        self.name = name
        self.species = species
        self.num_legs = num_legs
        self.num_ears = num_ears
        self.weight_kgs = weight_kgs
        self.num_works_art = num_works_art
        self.is_available = is_available
        self.skill_list = skill_list     
        self.previous_donations = previous_donations       
        self.create_date = datetime.datetime.now()

    def __str__(self):
        """Built-in method to return a string describing this instance"""
        s0 = f"I'm {self.name}.\n"
        s1 = f"I'm a {self.species} with {self.num_legs} legs and {self.num_ears} ear(s).\n"
        s2 = f"I weigh {self.weight_kgs:.2f} kgs.\n"
        s3 = f"I've been alive for {self.get_age_string()}.\n"
        s4 = f"I've created over {self.num_works_art} works of art."

        if self.is_available:
            s5 = "I'm available for tutoring.\n"
        else:
            s5 = "I'm already helping others learn Python.\n"

        s6 = "I know:\n"

        s7 = ""
        for skill in self.skill_list:
            s7 = s7 + f"  - {skill}\n"

        s8 = f"If you double the number of art works I have created you get {self.get_double_num_works_art()}.\n"
        
        s10 = f" and the average of my dontaions is {self.get_mean_donations():.2f}"

        s9 = "My previous donations include, "
        for donation in self.previous_donations: 
            s9 = s9 + f"{donation}, "
        
        


        s = s0 + s1 + s2 + s3 + s4 + s5 + s6 + s7 + s8 + s9 + s10
        return s
       
    def get_age_string(self):
        """Return the age as a string."""
        start = self.create_date
        end = datetime.datetime.now()
        duration = end - start
        ageString = str(duration)
        return ageString

    def get_double_num_works_art(self):
        """double the number of works of art"""
        double_art = self.num_works_art * 2
        return double_art

    def get_mean_donations(self):
        """average of donations"""
        donation_mean = stats.mean(self.previous_donations)
        return donation_mean

    def display_welcome(self):
        print()
        print("Welcome, I'm a new PyBuddy.\n")
        # print using our built-in to string method
        print(self.__str__())

        final_message = """

        You'll need curiousity, the ability to search the web,
        and the tenacity and resourcefulness
        to solve all kinds of challenges.

        Let's get started!

        """
        print(final_message)




# -------------------------------------------------------------
# Call some functions and execute code!

# if this is the main file being run

if __name__ == "__main__":
    # Create an instance of a PyBuddy
    alice = PyBuddy(
        "Alice",
        Species.CAT,
        4,
        2,
        8.123456,
        0,
        True,
        ["Git", "GitHub", "Python", "Markdown", "VS Code"],
        [5,10,7,15,25,50],
    )

    # Call the buddy's welcome() method
    alice.display_welcome()


    # Create another instance of a PyBuddy
    # using named arguments so it's clear what we're doing
    rex = PyBuddy(
        name="Rex",
        species=Species.DOG,
        num_legs=4,
        num_ears=2, 
        weight_kgs=10.437241,
        num_works_art= 0,
        is_available=True,
        skill_list=["Git", "GitHub", "Python", "Markdown", "VS Code"],
        previous_donations=[0,2,3],
        )

    rex.display_welcome()

if __name__ == "__main__":
    # Create an instance of a PyBuddy
    Vincent = PyBuddy(
        "Vincent",
        Species.ARTIST,
        2,
        1,
        75.2356,
        900,
        False,
        ["Painting", "Warm", "Cool", "Self Portraits", "Being Dramatic"],
        [2,3,9,7,1,4,5],
    )

    # Call the buddy's welcome() method
    Vincent.display_welcome()
