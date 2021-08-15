import unittest
from src.profile import Profile # changed from *
from src.movie import *

class TestProfile(unittest.TestCase):

    def setUp(self):

        # Creating some objects to use in the tests
        self.movie_1 = Movie("The Fugitive", "Andrew Daivs", 9)
        self.movie_2 = Movie("Hunger Games", "Gary Ross", 7)
        self.profile_1 = Profile("harrisonF", "myP@assword")


    # Test a Profile can add a favourite Movie
    def test_movie_starts_empty(self):
        self.assertEqual([], self.profile_1.favourites)
    def test_can_add_movie(self):
        self.profile_1.add_favourite(self.movie_1)
        self.assertEqual(1, len(self.profile_1.favourites))
    
    # Test a Profile can remove a given Movie from favourites
    def test_can_remove_movie(self):
        self.profile_1.add_favourite(self.movie_1)
        self.profile_1.remove_favourite(self.movie_1)
        self.assertEqual(0, len(self.profile_1.favourites))
    
    # Test a Profile can return a list of Favourites
    def test_can_return_list(self): # movie_1 # my idea
        self.profile_1.add_favourite(self.movie_2)
        self.assertEqual(self.profile_1.get_favourites()[0], self.movie_2)
        self.assertEqual(len(self.profile_1.get_favourites()), 1) # it does not matter when the calue 1 is before or after len function
        #self.profile_1.favourite_movies(self.movie_1) # my idea wrong