#!/usr/bin/env python

from lib.data_structures import get_names, get_spiciest_foods, print_spicy_foods,\
                                get_spicy_food_by_cuisine, sort_by_heat, \
                                print_spiciest_foods, get_average_heat_level

class TestDataStructures:
    '''Module data_structures.py'''

    SPICY_FOODS = [
        {
            "name": "Green Curry",
            "cuisine": "Thai",
            "heat_level": 9,
        },
        {
            "name": "Buffalo Wings",
            "cuisine": "American",
            "heat_level": 3,
        },
        {
            "name": "Mapo Tofu",
            "cuisine": "Sichuan",
            "heat_level": 6,
        }
    ]

    def test_get_names(self):
        '''contains function get_names() that retrieves names from list of foods.'''
        assert(get_names(TestDataStructures.SPICY_FOODS) == ['Green Curry', 'Buffalo Wings', 'Mapo Tofu'])

    def test_get_spiciest_foods(self):
        '''contains function get_spiciest_foods() that returns foods with a heat_level over 5.'''
        for food in get_spiciest_foods(TestDataStructures.SPICY_FOODS):
            assert(food["heat_level"]) > 5
    
    def test_print_spicy_foods(self):
        '''contains function print_spicy_foods that returns all foods formatted with 🌶 emojis.'''
        pass
