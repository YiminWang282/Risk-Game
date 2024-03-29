import unittest
from Item import Item
import io
import unittest.mock

class TestItem(unittest.TestCase):
    def test_item_define(self):
        #define item
        item = Item("bomb", 1, 2, 0, 4, "weapon", "test")

        self.assertEqual(item.getName(),"bomb")
        self.assertEqual(item.weight,1)
        self.assertEqual(item.getdamage(),2)
        self.assertEqual(item.cure,0)
        self.assertEqual(item.getPrice(),4)
        self.assertEqual(item.type,"weapon")

    def test_item_use_method(self):
        # Create an instance of the Item class
        item = Item("Little-knife", 3, 3, 0, 3, "weapon", "the weight is 3g, have 3 points of damage value.")

        # Capture the print output when the use method is called
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            damage = item.use()

        # Check if the print statement is correct
        self.assertIn(f"You have used {item.getName()}", mock_stdout.getvalue())

        # Check if the damage returned by the use method is correct
        self.assertEqual(damage, item.getdamage())

if __name__ == '__main__':
    unittest.main()




