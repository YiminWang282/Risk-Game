import unittest
from Store import Store
from Player import Player
from Item import Item

class TestStore(unittest.TestCase):
    def setUp(self):
        self.store = Store()  # Create a Store instance for testing
        self.player = Player(health=100, health_max=100, max_inventory_size=5, money=50)  # Create a Player instance for testing

    def test_buy_product_valid(self):
        # Add products to the store
        product1 = Item("Little-knife", 3, 3, 0, 3, "weapon", "the weight is 3g,have 3 points of damage value.")
        self.store.product.append(product1)

        initial_money = self.player.getMoney()

        # Attempt to buy a product with enough money and space in the inventory
        self.store.buyProduct(self.player, 0)

        # Check if the player's money has been deducted and the product is in the player's inventory
        self.assertEqual(self.player.getMoney(), initial_money - product1.getPrice())
        self.assertIn(product1, self.player.getInventory())

    def test_product_by_not_enough_money(self):
        product2 =Item("BIG-BOMB",1,1,1,100,"weapon","test")
        self.store.product.append(product2)

        initial_money = self.player.getMoney()

        self.store.buyProduct(self.player, 0)

        self.assertEqual(self.player.getMoney(), initial_money)
        self.assertNotIn(product2,self.player.getInventory())

    def test_buy_product_invalid(self):
        product2 =Item("BIG-BOMB",1,1,1,100,"weapon","test")
        self.store.product.append(product2)
        self.store.buyProduct(self.player,1)
        self.assertNotIn(product2,self.player.getInventory())


    




if __name__ == '__main__':
    unittest.main()
