# player.py
from Item import Item

class Player:
    def __init__(self,health,health_max,max_inventory_size,money):
        self.currentRoom = None  # location
        self.health =health
        self.inventory = []       # inventory
        self.health_max = health_max
        self.max_inventory_size = max_inventory_size
        self.money = money

    def getMoney(self):
        """
        return money
        """
        return self.money


    # # set the location of player
    # def setCurrentRoom(self, room):
    #     self.currentRoom = room
    #
    # # got the location of player
    # def getCurrentRoom(self):
    #     return self.currentRoom

    #show size of inventory
    def inventory_size(self):
        """
        :return: show the package size
        """
        return self.max_inventory_size

    # add items to the player's backpack
    def addToInventory(self, item):
        """
        add item into inventory
        :param item:
        :return: bool
        """
        if not self.isInventoryFull():
            self.inventory.append(item)
            self.max_inventory_size -= item.weight
            return True  # successfully added
        else:
            return False  # backpack is fulled

    # remove items from backpack
    def removeFromInventory(self, weapon):
        #after used weapon we need to remove it
        for item in self.inventory:
            if item ==weapon:
                self.inventory.remove(weapon)
                self.max_inventory_size += item.weight
                break

        return False  # can not find the item

    # show what kind of stuff in backpack
    def getInventory(self):
        #show inventory
        return self.inventory

    def get_reword(self, reward):
        #add reword to money
        self.money += reward

    def show_money(self):
        #show how many money in the inventory
        return self.money

    def substractMoney(self,price):
        #after using ,sub the money with price
        self.money-=price

    def isInventoryFull(self):
        #check the inventory
        return len(self.inventory) == self.max_inventory_size

    def haskey(self,item_name):
        #check the package if it has key
        for item in self.inventory:
            if item.getName() == item_name:
                return True
        return False

    def heal(self,medicine_heal):
        #use medicine to cure
        if self.health<self.health_max:
            if self.health+medicine_heal>=self.health_max:
                self.health=self.health_max
            else:
                self.health+=medicine_heal
            print(f"Now your health is {self.health}")
        else:
            print("You are healthy enough, you don't need heal!\n")


    def getItemByName(self,item_name):
        #get item from inventory
        for item in self.inventory:
            if item_name == item_name:
                return item
        return None


    def isDead(self):
        #check if player died
        if self.health<=0:
            return True
        else:
            return False
