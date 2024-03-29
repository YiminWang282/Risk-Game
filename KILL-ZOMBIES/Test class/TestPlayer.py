import unittest
from Player import Player
from Item import Item
from unittest.mock import patch
import io


class TestPlayer(unittest.TestCase):
    def setUp(self):
        # Set up a Player instance for testing
        self.player = Player(health=100, health_max=200, max_inventory_size=10, money=50)

    def test_initialization(self):
        # Test if the player is initialized correctly
        self.assertEqual(self.player.health, 100)
        self.assertEqual(self.player.health_max, 200)
        self.assertEqual(self.player.max_inventory_size, 10)
        self.assertEqual(self.player.money, 50)
        self.assertIsNone(self.player.currentRoom)
        self.assertFalse(self.player.isDead())
        self.assertFalse(self.player.isInventoryFull())

    def test_add_to_inventory(self):
        # Test adding items to the player's inventory
        item = Item("TestItem", 2, 5, 0, 10, "weapon", "Test description")
        added = self.player.addToInventory(item)
        self.assertTrue(added)
        self.assertIn(item, self.player.inventory)
        self.assertEqual(self.player.max_inventory_size, 8)

    def test_remove_from_inventory(self):
        # Test removing items from the player's inventory
        item = Item("TestItem", 2, 5, 0, 10, "weapon", "Test description")
        self.player.addToInventory(item)
        removed = self.player.removeFromInventory(item)
        self.assertFalse(removed)
        self.assertNotIn(item, self.player.inventory)
        self.assertEqual(self.player.max_inventory_size, 10)

    def test_remove_nonexistent_from_inventory(self):
        # Test removing a nonexistent item from the player's inventory
        item = Item("NonexistentItem", 2, 5, 0, 10, "weapon", "Test description")
        removed = self.player.removeFromInventory(item)
        self.assertFalse(removed)

    def test_get_inventory(self):
        # Test getting the player's inventory
        item1 = Item("Item1", 2, 5, 0, 10, "weapon", "Test description")
        item2 = Item("Item2", 3, 7, 0, 15, "weapon", "Test description")
        self.player.addToInventory(item1)
        self.player.addToInventory(item2)
        inventory = self.player.getInventory()
        self.assertIn(item1, inventory)
        self.assertIn(item2, inventory)

    def test_get_reword(self):
        # Test getting a reward
        self.player.get_reword(20)
        self.assertEqual(self.player.money, 70)

    def test_subtract_money(self):
        # Test subtracting money from the player
        self.player.substractMoney(30)
        self.assertEqual(self.player.money, 20)

    def test_has_key(self):
        # Test checking if the player has a specific key item
        key_item = Item("Key", 1, 0, 0, 0, "key", "Test key description")
        self.player.addToInventory(key_item)
        self.assertTrue(self.player.haskey("Key"))
        self.assertFalse(self.player.haskey("NonexistentKey"))

    def test_heal(self):
        # Test healing the player
        self.player.health = 150
        self.player.heal(30)
        self.assertEqual(self.player.health, 180)

    def test_heal_max_health(self):
        # Test healing the player when already at max health
        self.player.health = 200
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            self.player.heal(30)
        self.assertIn("You are healthy enough, you don't need heal!", mock_stdout.getvalue())
        self.assertEqual(self.player.health, 200)

    def test_get_item_by_name(self):
        # Test getting an item from the player's inventory by name
        item = Item("TestItem", 2, 5, 0, 10, "weapon", "Test description")
        self.player.addToInventory(item)
        found_item = self.player.getItemByName("TestItem")
        self.assertEqual(found_item, item)

    def test_get_nonexistent_item_by_name(self):
        # Test getting a nonexistent item from the player's inventory by name
        found_item = self.player.getItemByName("NonexistentItem")
        self.assertIsNone(found_item)

    def test_is_dead(self):
        # Test checking if the player is dead
        self.assertFalse(self.player.isDead())
        self.player.health = 0
        self.assertTrue(self.player.isDead())

if __name__ == '__main__':
    unittest.main()
