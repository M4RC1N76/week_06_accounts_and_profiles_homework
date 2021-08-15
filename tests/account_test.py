import unittest
from src.account import *
from src.profile import *

class TestAccount(unittest.TestCase):

    def setUp(self):
        # Creating some objects to use in the tests
        self.profile_1 = Profile("harrisonF", "myP@assword")
        self.profile_2 = Profile("markH", "anotherP@ssword")
        self.account_1 = Account(
            "Jane", "Smith", "janes@email.com", []) # added and profile removed

        

    # Test an Account can add a Profile
    def test_can_add_profiles(self):
        self.account_1.add_profile(self.profile_1) # throws an error line 18
        self.assertEqual(1, len(self.account_1.profiles))
        # self.profile_1.add_profile(self.profile_1) wrongly used (add_profile)
        # self.assertEqual(1, len(self.profile_1.favourites)) wrong
    
    # Test an Account can remove a given Profile
    def test_can_remove_given_profile(self):
        self.account_1.add_profile(self.profile_2)
        self.account_1.remove_profile(self.profile_2)
        self.assertEqual(0, len(self.account_1.profiles))
    
    # Test an Account can return a list of Profiles
    def get_profiles(self):
        self.account_1.add_profile(self.profile_2)
        self.assertEqual(self.account_1.get_profiles()[0], self.profile_2)
        self.assertEqual(len(self.account_1.get_profiles()), 1)





    # Test a Profile can add a favourite Movie

#    def test_movie_starts_empty(self):
        # self.assertEqual([], self.profile_1.favourites)

    # def test_can_add_movie(self):
        # self.profile_1.add_favourite_movie(self.movie_1)
        # self.assertEqual(1, len(self.profile_1.favourites))

    # Test a Profile can remove a given Movie from favourites
    # def test_can_remove_movie(self):
        # self.profile_1.add_favourite_movie(self.movie_2)
        # self.profile_1.remove_favourite_movie(self.movie_2)
        # self.assertEqual(0, len(self.profile_1.favourites))
    # Test a Profile can return a list of Favourites

    # def test_can_return_list(self):
        # self.
