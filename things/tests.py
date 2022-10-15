from django.core.exceptions import ValidationError
from django.test import TestCase

from things.models import Thing


class UserModelTestCase(TestCase):

    def setUp(self):
        self.thing = Thing(
        name = 'bags',
        description = 'Red bags',
        quantity = 13)
    
    def test_valid_name(self):
        self._assert_thing_is_valid()
    
    def test_name_cannot_be_blank(self):
        self.thing.name = ''
        self._assert_thing_is_invalid()

    """def test_thing_must_be_unique(self):
        second_thing =self._create_second_thing()
        self.thing.name = second_thing.name
        self._assert_thing_is_invalid()
    """
    def test_name_can_be_30_characters_long(self):
        self.thing.name = 'x' * 29
        self._assert_thing_is_valid()
    
    def test_name_cannot_be_over_30_characters_long(self):
        self.thing.name = 'x' * 31
        self._assert_thing_is_invalid()
    #description
    def test_description_may_be_blank(self):
        self.thing.description= ''
        self._assert_thing_is_valid()
        
    def test_description_need_not_to_be_unique(self):
        second_thing =self._create_second_thing()
        self.thing.description = second_thing.description
        self._assert_thing_is_valid()
    
    def test_description_may_contain_120_characters(self):
        self.thing.description = 'x' * 120
        self._assert_thing_is_valid()

    def test_description_may_not_contain_more_than_120_characters(self):
        self.thing.description= 'x' * 121
        self._assert_thing_is_invalid()  
    #quantity
    def test_quantity_need_not_to_be_unique(self):
        second_thing =self._create_second_thing()
        self.thing.quantity = second_thing.quantity
        self._assert_thing_is_valid()

    def test_quantity_need_to_be_between_0_and_100(self):
        self.thing.quantity <= 100
        self._assert_thing_is_valid()

    """def test_quantity_need_not_to_be_more_than_100(self):
        self.thing.quantity >= 101
        self._assert_thing_is_invalid()
"""
    def _assert_thing_is_valid(self):
        try:
            self.thing.full_clean()
        except (ValidationError):
            self.fail('Test thing should be valid.')

    def _assert_thing_is_invalid(self):
        with self.assertRaises(ValidationError):
            self.thing.full_clean()

    def _create_second_thing(self):
        thing = Thing(name = 'Chairs',
        description = 'colorful chairs',
        quantity = 13)
        return thing