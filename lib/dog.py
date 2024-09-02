#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    BREEDS = ["Labrador", "Poodle", "Bulldog", "Beagle", "Pug"]  
    
    def __init__(self, name='Fido', breed='Bulldog'):
        self._name = None
        self._breed = None
        self.name = name
        self.breed = breed
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value) == 0 or len(value) > 25:
            print("Name must be string between 1 and 25 characters.")
        else:
            self._name = value
    
    @property
    def breed(self):
        return self._breed
    
    @breed.setter
    def breed(self, value):
        if value not in self.BREEDS:
            print("Breed must be in list of approved breeds.")
        else:
            self._breed = value
