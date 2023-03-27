# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 22:48:58 2023

@author: shind
"""

#user management system
class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
        self.profile = {}

    def create_profile(self, name, bio, location):
        self.profile = {"name": name, "bio": bio, "location": location}

class UserManagement:
    def __init__(self):
        self.users = {}

    def create_user(self, username, password, email):
        if username not in self.users:
            self.users[username] = User(username, password, email)
            return True
        else:
            return False

    def login(self, username, password):
        if username in self.users:
            user = self.users[username]
            if user.password == password:
                return user
        return None

    def update_profile(self, user, name=None, bio=None, location=None):
        if name:
            user.profile["name"] = name
        if bio:
            user.profile["bio"] = bio
        if location:
            user.profile["location"] = location

import unittest

class TestUserManagement(unittest.TestCase):

    def setUp(self):
        self.user_management = UserManagement()
        self.user1 = User("user1", "password1", "user1@example.com")
        self.user2 = User("user2", "password2", "user2@example.com")
        self.user_management.create_user("user1", "password1", "user1@example.com")

    def test_create_user(self):
       
        self.assertTrue(self.user_management.create_user("user2", "password2", "user2@example.com"))

       
        self.assertFalse(self.user_management.create_user("user1", "password1", "user1@example.com"))

    def test_login(self):
        

       
        self.assertIsNone(self.user_management.login("user3", "password3"))

        
        self.assertIsNone(self.user_management.login("user1", "password2"))

    def test_update_profile(self):
       
        self.user_management.update_profile(self.user1, name="User One", bio="A bio", location="New York")
        self.assertEqual(self.user1.profile, {"name": "User One", "bio": "A bio", "location": "New York"})

       
        self.user_management.update_profile(self.user1, bio="Another bio")
        self.assertEqual(self.user1.profile, {"name": "User One", "bio": "Another bio", "location": "New York"})
        
if __name__=="__main__":
    unittest.main()        