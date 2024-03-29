import unittest
from Room import Room
from Item import Item
from Player import Player
from Zombie import Zombie

class TestRoom(unittest.TestCase):
    def setUp(self):
        #define room,item,zombie
        self.room = Room("Test Room", "This is a test room.")
        self.item = Item("Test Item", 5, 2, 0, 10, "weapon", "Test item description.")
        self.zombie = Zombie("Test Zombie", 20, 5,5)

    #check the direction is correct
    def test_set_exit(self):
        self.room.setExit("north", Room("North Room", "This is the north room."))
        self.assertEqual(self.room.getExits(), ["north"])

    #test add_items
    def test_add_items(self):
        self.room.add_items(self.item)
        self.assertEqual(self.room.getItems(), ["Test Item"])

    #test add_zombie
    def test_add_zombie(self):
        self.room.addZombie(self.zombie)
        self.assertEqual(self.room.getZombies(), [self.zombie])

    #test remove_zombie
    def test_remove_zombie(self):
        self.room.addZombie(self.zombie)
        self.room.removeZombie(self.zombie)
        self.assertEqual(self.room.getZombies(), [])

    #test has_zombies
    def test_has_zombies(self):
        self.assertFalse(self.room.haszombies())
        self.room.addZombie(self.zombie)
        self.assertTrue(self.room.haszombies())

    #test get_short_description
    def test_get_short_description(self):
        self.assertEqual(self.room.getShortDescription(), "This is a test room.")

    #test take_item
    def test_take_item(self):
        player = Player(100, 100, 10, 50)
        self.room.add_items(self.item)
        taken_item = self.room.takeItem("Test Item", player)
        self.assertEqual(taken_item, self.item)
        self.assertEqual(self.room.getItems(), [])
        self.assertEqual(player.getInventory(), [self.item])


if __name__ == "__main__":
    unittest.main()
