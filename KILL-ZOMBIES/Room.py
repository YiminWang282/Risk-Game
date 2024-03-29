"""
    Create a room described "description". Initially, it has
    no exits. 'description' is something like 'kitchen' or
    'an open court yard'
"""
from Player import Player

class Room:

    def __init__(self,name, description):
        """
            Constructor method
        :param description: text description for this room
        """
        self.name = name
        self.description = description
        self.exits = {}     # Dictionary
        self.items = []
        self.background_description = ""  # the background of room
        self.zombies = []  # zombies in the room

    def setExit(self, direction, neighbour):
        """
            Adds an exit for a room. The exit is stored as a dictionary
            entry of the (key, value) pair (direction, room)
        :param direction: The direction leading out of this room
        :param neighbour: The room that this direction takes you to
        :return: None
        """
        self.exits[direction] = neighbour

    def getName(self):
        #get name
        return self.name
    def add_items(self,Item):
        #add item into room
        self.items.append(Item)

    def addZombie(self, zombie):
        #add zombie into toom
        self.zombies.append(zombie)

    def removeZombie(self, zombie):
        self.zombies.remove(zombie)
        if self.zombies==None:
            print("Now you killed all zombies in this room, you can take the weapons in this room!")

    def haszombies(self):
        return bool(self.zombies)

    def getShortDescription(self):
        """
            Fetch a short text description
        :return: text description
        """
        return self.description

    def getLongDescription(self):
        """
            Fetch a longer description including available exits
        :return: text description
        """
        zombie_info = ""
        for zombie in self.zombies:
            zombie_info += f"{zombie.name} (Blood:{zombie.zombie_health()}) \n"

        items = self.getItems()
        description = f'Location: {self.description}, you can choose go: {self.getExits()}\n'
        if not zombie_info:
            #if its empty
            description+= f"There's no zombie in this room now!\n"
        else:
            description += f"Zombies: {zombie_info}"


        if items:
            items_str = ", ".join(items)
            description += f'Items in the room: {items_str}\n'
        else:
            description += "There are no items in this room.\n"

        return description



    def getExits(self):
        """
            Fetch all available exits as a list
        :return: list of all available exits
        """
        allExits = self.exits.keys()
        return list(allExits)

    def getExit(self, direction):
        """
            Fetch an exit in a specified direction
        :param direction: The direction that the player wishes to travel
        :return: Room object that this direction leads to, None if one does not exist
        """
        if direction in self.exits:
            return self.exits[direction]
        else:
            return None

    def getItems(self):
        """
        got the list in the room
        :return: Item in the room
        """
        return [item.getName() for item in self.items]

    def takeItem(self,item_name,Player):
        """
        take the Item from room
        :param item_name: name of item
        :return: the item be take,if nun then return none
        """
        for item in self.items:
            if item.getName() == item_name:
                Player.addToInventory(item)

                self.items.remove(item)
                return item
        return None



    def getZombies(self):
        #check how many zombies in the room
        return self.zombies

