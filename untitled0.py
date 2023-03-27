# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 22:29:21 2023

@author: shind
"""

import unittest
import json
import os

def create_art_space(name, location, description):
    # Create a dictionary to hold the art space details
    art_space = {
        'name': name,
        'location': location,
        'description': description
    }

    # Open the file to store the art space details
    with open('art_spaces.json', 'a') as file:
        # Write the art space details to the file
        file.write(json.dumps(art_space))
        file.write('\n') # add a newline character to separate entries

    # Return a message indicating success
    return f'Art space {name} created successfully!'



class TestArtSpace(unittest.TestCase):

    def setUp(self):
       
        self.filepath = 'art_spaces.json'
        with open(self.filepath, 'w') as file:
            file.write('')

    def tearDown(self):
      
        os.remove(self.filepath)

    def test_create_art_space(self):
       
        name = 'Test Art Space'
        location = 'Test Location'
        description = 'Test Description'

     
        result = create_art_space(name, location, description)

      
        expected_output = f'Art space {name} created successfully!'
        self.assertEqual(result, expected_output)

       
        with open(self.filepath, 'r') as file:
            art_spaces = [json.loads(line) for line in file]
            self.assertEqual(len(art_spaces), 1)
            self.assertEqual(art_spaces[0]['name'], name)
            self.assertEqual(art_spaces[0]['location'], location)
            self.assertEqual(art_spaces[0]['description'], description)

if __name__ == "__main__":
    unittest.main()