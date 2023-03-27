# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 22:59:15 2023

@author: shind
"""

def create_programming( name, description, category, date, location, performers):
    # logic to create a new programming item in the database
    global programming_item
    programming_item = {
        'name': name,
        'description': description,
        'category': category,
        'date': date,
        'location': location,
        'performers': performers
    }
    # save the programming item in the database
    # return the ID of the new programming item
    return id(programming_item)

def get_programming(id):
    # logic to get a programming item from the database using its ID
    return programming_item

def update_programming(id, name=None, description=None, category=None, date=None, location=None, performers=None):
    # logic to update a programming item in the database using its ID
    programming_item = get_programming(id)
    if name:
        programming_item['name'] = name
    if description:
        programming_item['description'] = description
    if category:
        programming_item['category'] = category
    if date:
        programming_item['date'] = date
    if location:
        programming_item['location'] = location
    if performers:
        programming_item['performers'] = performers
    # save the updated programming item in the database
    return programming_item

def delete_programming(id):
    # logic to delete a programming item from the database using its ID
    # return True if the item was deleted successfully, False otherwise
    return 'deleted_successfully'


import unittest

class TestProgrammingManagement(unittest.TestCase):

    def test_create_programming(self):
        result = create_programming('Test Programming', 'This is a test programming item', 'music', '2023-04-01', 'New Delhi', ['performer1', 'performer2'])
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)

    def test_get_programming(self):
        id = create_programming('Test Programming', 'This is a test programming item', 'music', '2023-04-01', 'New Delhi', ['performer1', 'performer2'])
        result = get_programming(id)
        self.assertIsNotNone(result)

    def test_update_programming(self):
        id = create_programming('Test Programming', 'This is a test programming item', 'music', '2023-04-01', 'New Delhi', ['performer1', 'performer2'])
        result = update_programming(id, name='Updated Programming', location='Mumbai')
        self.assertIsNotNone(result)
        self.assertEqual(result['name'], 'Updated Programming')
        self.assertEqual(result['location'], 'Mumbai')

    def test_delete_programming(self):
        id = create_programming('Test Programming', 'This is a test programming item', 'music', '2023-04-01', 'New Delhi', ['performer1', 'performer2'])
        result = delete_programming(id)
        self.assertTrue(result)
if __name__=="__main__":
    unittest.main()                
        