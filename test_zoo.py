import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()

    def test_child_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(5), 50)
       
    # Add your additional test cases here.

    def test_schoolage_tickey_price(self):
        self.assertEqual(self.zoo.get_ticket_price(18), 100)
    
    def test_adult_tickey_price(self):
        self.assertEqual(self.zoo.get_ticket_price(55), 150)
    
    def test_oldage_tickey_price(self):
        self.assertEqual(self.zoo.get_ticket_price(80), 100)

    def test_noage_tickey_price(self):
        self.assertEqual(self.zoo.get_ticket_price(-1), 'invalid')
    


if __name__ == '__main__':
    unittest.main()