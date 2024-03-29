import unittest
from Zombie import Zombie
from Player import Player

class TestZombie(unittest.TestCase):
    def setUp(self):
        # define zombie
        self.zombie = Zombie("Test Zombie", 20, 10, 5)

    def test_take_damage(self):
        # test take_damage function
        reward = self.zombie.takeDamage(15)
        # ensure return reward
        self.assertEqual(reward, 0)
        # ensure the health of zombie is decreasing
        self.assertEqual(self.zombie.zombie_health(), 5)

    def test_attack_player(self):
        # define player
        player = Player(100, 100, 10, 0)
        # test attackplayer
        self.zombie.attackPlayer(player)
        # ensure the health of player is decreasing
        self.assertEqual(player.health, 95)

if __name__ == '__main__':
    unittest.main()
