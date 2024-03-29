from Room import Room
from TextUI import TextUI
from Player import Player
from Item import Item
from Zombie import Zombie
from Store import Store
import random

"""
    This class is the main class of the "Adventure World" application. 
    'Adventure World' is a very simple, text based adventure game.  Users 
    can walk around some scenery. That's all. It should really be extended 
    to make it more interesting!
    
    To play this game, create an instance of this class and call the "play"
    method.

    This main class creates and initialises all the others: it creates all
    rooms, creates the parser and starts the game.  It also evaluates and
    executes the commands that the parser returns.
    
    This game is adapted from the 'World of Zuul' by Michael Kolling
    and David J. Barnes. The original was written in Java and has been
    simplified and converted to Python by Kingsley Sage
"""
class Game:
    def __init__(self):
        """
        Initialises the game
        """
        self.createRooms()
        self.currentRoom = self.saferoom
        self.textUI = TextUI()
        self.player = Player(20,20,50,20) #set the player
        self.creatItems()
        self.store = Store()
        self.initializeGame()



    def initializeGame(self):#restart game
        self.createRooms()
        self.currentRoom = self.saferoom
        self.textUI = TextUI()
        self.player = Player(20,20,50, 20)
        self.creatItems()

    def createRooms(self):
        """
            Sets up all room assets
        :return: None
        """
        #show the name of area
        self.saferoom = Room("saferoom","You are in the safe room now,you can go east.")
        self.firststreet = Room("firststreet","In the first street")
        self.policestation = Room("policestation","In the police station")
        self.supermarket = Room("supermarket","In a supermarket")
        self.secondStreet = Room("secondStreet","Now,you're in the second street")
        self.campus = Room("campus","At the school campus")
        self.firstfloor = Room("firstfloor","Inside the academic building -first floor")
        self.basement = Room("basement","In the basement")
        self.secondfloor= Room("secondfloor","Now you are in the second floor")
        self.rooftop = Room("rooftop","On the rooftop")

        #defined zombies
        zombie_1 = Zombie("weak-zombie", 3, 5,1)
        zombie_7 = Zombie("little-zombie",4,7,2)
        zombie_2 = Zombie("normal-zombie", 5, 8,2)
        zombie_3 = Zombie("strong-zombie", 10, 10,3)
        zombie_4 = Zombie("twins_zombie",15,20,4)
        zombie_5 = Zombie("crazy-zombie",3,8,4)
        zombie_6 = Zombie("huge-zombie",10,10,3)
        zombie_8 = Zombie("small-zombie",3,4,1)
        zombie_9 = Zombie("quite-zombie",3,5,1)
        zombie_10 = Zombie("cute-zombie", 3, 5, 1)
        zombie_11 = Zombie("calm-zombie", 3, 5, 1)


        #addzombies
        self.firststreet.addZombie(zombie_1)
        self.policestation.addZombie(zombie_8)
        self.policestation.addZombie(zombie_2)
        self.supermarket.addZombie(zombie_9)
        self.supermarket.addZombie(zombie_3)
        self.secondStreet.addZombie(zombie_10)
        self.secondStreet.addZombie(zombie_11)
        self.secondStreet.addZombie(zombie_4)
        self.campus.addZombie(zombie_5)
        self.firstfloor.addZombie(zombie_6)
        self.secondfloor.addZombie(zombie_7)


        # createitem
        self.creatItems()

        # add item to room
        self.firststreet.add_items(self.little_knife)
        self.firststreet.add_items(self.little_cure)
        self.policestation.add_items(self.little_knife)
        self.supermarket.add_items(self.little_knife)
        self.secondStreet.add_items(self.gun)
        self.secondStreet.add_items(self.first_aid_kit)
        self.campus.add_items(self.big_knife)
        self.firstfloor.add_items(self.gun)
        self.firstfloor.add_items(self.first_aid_kit)
        self.secondfloor.add_items(self.gun)
        self.basement.add_items(self.final_key)

        #set exit for every room
        self.saferoom.setExit("east", self.firststreet)
        self.firststreet.setExit("west",self.saferoom)
        self.firststreet.setExit("south", self.supermarket)
        self.supermarket.setExit("north",self.firststreet)
        self.firststreet.setExit("north", self.policestation)
        self.policestation.setExit("south",self.firststreet)
        self.firststreet.setExit("east", self.secondStreet)
        self.secondStreet.setExit("west",self.firststreet)
        self.secondStreet.setExit("east", self.campus)
        self.campus.setExit("west",self.secondStreet)
        self.campus.setExit("south", self.firstfloor)
        self.firstfloor.setExit("upstairs", self.secondfloor)
        self.firstfloor.setExit("north",self.campus)
        self.secondfloor.setExit("upstairs",self.rooftop)
        self.secondfloor.setExit("downstairs",self.firstfloor)
        self.firstfloor.setExit("downstairs", self.basement)
        self.rooftop.setExit("downstairs",self.secondfloor)
        self.basement.setExit("upstairs", self.firstfloor)

    #creaitem
    def creatItems(self):
        self.little_knife = Item("Little-knife", 3, 3, 0,3,"weapon","the weight is 3g,have 3 points of damage value. ")
        self.big_knife = Item("Big-knife", 5, 5, 0,5,"weapon","the weight is 5g,have 5 points of damage value.")
        self.sword= Item("sword",7,7,0,7,"weapon","the weight is 7g,have 7 points of damage value.")
        self.gun = Item("Gun", 10, 10, 0,10,"weapon","the weight is 10g,have 10 points of damage value.")
        self.final_key = Item("final-key", 10, 0,0, 10,"key","Got it, then you can escape from this city!!")
        self.little_cure = Item("little-cure",1,0,5,3,"medicine","the weight is 1g,can cure 5 heath.")
        self.first_aid_kit =Item("first_aid_kit",3,0,10,5,"medicine","the weight is 3g,can cure 10 heath.")


    #define the player from the start
    def play(self):
        """
            The main play loop
        :return: None
        """
        self.player.addToInventory(self.little_knife)
        self.player.addToInventory(self.little_cure)
        self.printWelcome()
        finished = False
        while (finished == False):
            command = self.textUI.getCommand()      # Returns a 2-tuple
            finished = self.processCommand(command)




    def printWelcome(self):
        """
            Displays a welcome message
        :return:
        """
        self.textUI.printtoTextUI("A virus has leaked from the city's labs and infected zombies roam the streets.")
        self.textUI.printtoTextUI("Your daughter has gotten separated and is trapped in the school basement.")
        self.textUI.printtoTextUI("Rescue operation, begin~")
        self.textUI.printtoTextUI("Operation Escape from the City!!!")
        self.textUI.printtoTextUI("")
        self.doInventoryCommand()
        self.textUI.printtoTextUI(f'Your command words are: {self.showCommandWords()}')
        self.textUI.printtoTextUI("If you need help about information, then use 'help' command.\n")
        self.textUI.printtoTextUI(self.currentRoom.getShortDescription())





    def showCommandWords(self):
        """
            Show a list of available commands
        :return: None
        """
        return ['go','inventory','help', 'quit']



    def showplayercomandwords(self):
        #show player's command to let player to choose
        return ['attack','go','inventory','take','store','quit','help']


    #it can be use of reply the command we set
    def processCommand(self, command):
        """
            Process a command from the TextUI
        :param command: a 2-tuple of the form (commandWord, secondWord)
        :return: True if the game has been quit, False otherwise
        """


        commandWord, secondWord = command
        if commandWord != None:
            commandWord = commandWord.upper()

        wantToQuit = False
        if commandWord == "HELP":
            self.doPrintHelp()
        elif commandWord == "GO":
            self.doGoCommand(secondWord)
        elif commandWord == "TAKE":
            self.doTakeCommand(secondWord)
        elif commandWord == "INVENTORY":
            self.doInventoryCommand()
        elif commandWord == "QUIT":
            wantToQuit = True
        elif commandWord == "ATTACK":
            if self.attackZombieCommand():
                self.textUI.printtoTextUI("You died!")
                return True
        elif commandWord == "INVENTORY":
            self.player.getInventory()
        elif commandWord == "STORE":
            self.doStoreCommand(self.store)
        elif commandWord == "THROW":
            self.dothrowCommand(secondWord)
        elif commandWord == "CURE":
            self.docureCommand()
        else: #if the command we did'n set
            self.textUI.printtoTextUI("Sorry, what do you mean?")
        #set the condition, how to win the game
        if self.currentRoom == self.rooftop: #when in the rooftop then you will win the game
            self.textUI.printtoTextUI("You rescued your daughter and escaped the city. You win!")
            return True
        #
        # if commandWord != "GO" and commandWord!="QUIT" and commandWord!="HELP":
        #     self.textUI.printtoTextUI(self.currentRoom.getLongDescription())
        #     self.textUI.printtoTextUI("Choose your command: "+'( ' + ', '.join(self.showplayercomandwords())+' )')


        #this is for quit the game
        return wantToQuit



    def doPrintHelp(self):
        """
            Display some useful help text
        :return: None
        """
        self.textUI.printtoTextUI("A virus has leaked from the city's labs and infected zombies roam the streets.")
        self.textUI.printtoTextUI("Your daughter has gotten separated and is trapped in the school basement.")
        self.textUI.printtoTextUI("")
        self.textUI.printtoTextUI("What you need to do?")
        self.textUI.printtoTextUI("At first time, you are in the safe room. And this room has no zombies.")
        self.textUI.printtoTextUI("When you getting into a new area, you need to defeated all the zombies in the area.")
        self.textUI.printtoTextUI("You can take the weapon from space without zombies.")
        self.textUI.printtoTextUI("Then you can go to next room.")
        self.textUI.printtoTextUI("In the academic building, you need to perish the zombies in second floor.")
        self.textUI.printtoTextUI("Before you go to the basement to save your daughter.")
        self.textUI.printtoTextUI("In the end, you need to buy a final-key, then you can escape to the rooftop.")
        self.textUI.printtoTextUI("There will have helicopter to save you to a safe city.")
        self.textUI.printtoTextUI("BTW, you can go back to front places before you clean the zombies.")
        self.textUI.printtoTextUI("")
        self.textUI.printtoTextUI("About command:")
        self.textUI.printtoTextUI("You can use 'attack' command to attack the zombies.")
        self.textUI.printtoTextUI("You can use 'go' with direction you what to go to another places.")
        self.textUI.printtoTextUI("You can use 'inventory' to show the stuffs, money and free package space.")
        self.textUI.printtoTextUI("You can use 'take' to take the weapon, after there's no zombie in the place.")
        self.textUI.printtoTextUI("You can use 'store' command to buy some stuff useful.")
        self.textUI.printtoTextUI("If you want to quit the game, then use 'quit' command.")
        self.textUI.printtoTextUI("Using 'help' command, you will see the info what you are reading now ~ ^_^!")
        self.textUI.printtoTextUI(f'Your command words are: {self.showCommandWords()}')

    """
    This is for the situation 
    if the player died,then you can choose the command yes/no
    """
    def player_dead(self):
        if self.player.isDead():
            choice = input("You died! Do you want to restart the game? (yes/no): ")
            if choice.lower() == "yes": #yes means restart the game
                self.initializeGame()
                self.play()
            else: #no means quit the game
                self.textUI.printtoTextUI("Thank you for playing!")
        else:
            return



    def doGoCommand(self, secondWord):
        """
            Performs the GO command
        :param secondWord: the direction the player wishes to travel in
        :return: None
        """
        discoveredlist = ["saferoom","firststreet"]

        if secondWord == None:
            # Missing second word ...
            self.textUI.printtoTextUI("Where you want to go?\n")
            return

        nextRoom = self.currentRoom.getExit(secondWord)
        if nextRoom == None: #if the nextroom word is wrong
            self.textUI.printtoTextUI("There is no such direction. Please choose the right direction!!\n")
        else:
            """
            If the next room 
            """
            if nextRoom.getName() in discoveredlist:
                self.currentRoom = nextRoom
                self.textUI.printtoTextUI(self.currentRoom.getLongDescription())
                if self.currentRoom.haszombies():
                    random_zombie = random.choice(self.currentRoom.zombies)
                    random_zombie.attackPlayer(self.player)
                    self.player_dead()
                self.textUI.printtoTextUI("Choose your command: " + '( ' + ', '.join(self.showplayercomandwords()) + ' )')


            else:
                """
            if has zombie in this room
            then you need to clear it first
            """
                if self.hasZombiesInRoom():
                    self.textUI.printtoTextUI(f"Sorry, you need to take out all zombies first.\n")
                else:
                    #just when having final-key then you can get into rooftop
                    if nextRoom.getName() =="rooftop":
                        if self.player.haskey("final-key"):
                            self.currentRoom = nextRoom
                            self.textUI.printtoTextUI(self.currentRoom.getLongDescription())
                            if self.currentRoom.haszombies():
                                random_zombie = random.choice(self.currentRoom.zombies)
                                random_zombie.attackPlayer(self.player)
                                self.player_dead()
                            #self.textUI.printtoTextUI("Choose your command: " + '( ' + ', '.join(self.showplayercomandwords()) + ' )')


                        else:
                            self.textUI.printtoTextUI("PLZ，go to the basement to save your daughter first!!!")
                            self.textUI.printtoTextUI("Plz got the key before you going to the rooftop.\n")

                    #before you go to basement, you need to clean the second floor
                    elif nextRoom.getName() == "basement":
                        if not self.secondfloor.haszombies():
                            discoveredlist.append(self.currentRoom.getName())
                            self.currentRoom = nextRoom
                            self.textUI.printtoTextUI(self.currentRoom.getLongDescription())
                            if self.currentRoom.haszombies():
                                random_zombie = random.choice(self.currentRoom.zombies)
                                random_zombie.attackPlayer(self.player)
                                self.player_dead()
                            self.textUI.printtoTextUI("Choose your command: " + '( ' + ', '.join(self.showplayercomandwords()) + ' )')
                            self.textUI.printtoTextUI("Now,you successfully rescued your daughter!!! Go to the rooftop.")

                        else:
                            self.textUI.printtoTextUI("Plz go to the second floor clear all the zombies first.\n")

                            self.textUI.printtoTextUI(self.currentRoom.getLongDescription())
                            self.textUI.printtoTextUI("Choose your command: " + '( ' + ', '.join(self.showplayercomandwords()) + ' )')
                    #before going to secondstreet you need to go to policestatin and supermarkets
                    elif nextRoom.getName() =="secondStreet":
                        if self.supermarket.haszombies() or self.policestation.haszombies():
                            self.textUI.printtoTextUI("Plz, clean the zombies in supermarket and policestation first.\n")
                            self.textUI.printtoTextUI(self.currentRoom.getLongDescription())
                            self.textUI.printtoTextUI("Choose your command: " + '( ' + ', '.join(self.showplayercomandwords()) + ' )')
                        else:
                            self.currentRoom = nextRoom
                            discoveredlist.append(self.currentRoom.getName())
                            self.textUI.printtoTextUI(self.currentRoom.getLongDescription())
                            if self.currentRoom.haszombies():
                                random_zombie = random.choice(self.currentRoom.zombies)
                                random_zombie.attackPlayer(self.player)
                                self.player_dead()
                            self.textUI.printtoTextUI(
                                "Choose your command: " + '( ' + ', '.join(self.showplayercomandwords()) + ' )')
                    else:
                        #after go to that place then we add into discoveredlist
                        self.currentRoom = nextRoom
                        discoveredlist.append(self.currentRoom.getName())
                        self.textUI.printtoTextUI(self.currentRoom.getLongDescription())
                        if self.currentRoom.haszombies():
                            random_zombie = random.choice(self.currentRoom.zombies)
                            random_zombie.attackPlayer(self.player)
                            self.player_dead()
                        self.textUI.printtoTextUI("Choose your command: " + '( ' + ', '.join(self.showplayercomandwords()) + ' )')


    #pick up the things from room
    def doTakeCommand(self, item_name):
        room_items = self.currentRoom.getItems()
        if item_name == None:
            # Missing second word ...
            self.textUI.printtoTextUI("Sorry. Please tell me what you want to take?\n")
            return


        if self.hasZombiesInRoom():#if has zombie in this room then can't go to new room
            self.textUI.printtoTextUI("You can't take items with zombies in the room.\n")
            return


        if item_name is not None and item_name in room_items:
            # there have item in the room
            item = self.currentRoom.takeItem(item_name,self.player)

            self.textUI.printtoTextUI(f"You've taken {item_name}.")
            self.textUI.printtoTextUI("Choose your command: " + '( ' + ', '.join(self.showplayercomandwords()) + ' )')
        else:
            self.textUI.printtoTextUI(f"Here is empty now.")

    def dothrowCommand(self,secondWord):
        if secondWord :
            #check if inventory have this item
            item_name= " ".join(secondWord)
            item_to_throw = self.player.getItemByName(item_name)

            if item_to_throw:
                #remove item
                self.player.removeFromInventory(item_to_throw)
                self.textUI.printtoTextUI(f"You have thrown {item_name}.\n")
            else:
                self.textUI.printtoTextUI(f"You don't have {item_name} in your inventory.\n")
        else:
            self.textUI.printtoTextUI("Please specify the item you want to throw.\n")



    def doStoreCommand(self,Store):
        #list the products in store
        Store.listProducts()
        try:
            product_index = int(input("Enter the product number you want to buy: "))
            Store.buyProduct(self.player,product_index)
            self.textUI.printtoTextUI("Choose your command: " + '( ' + ', '.join(self.showplayercomandwords()) + ' )')
        except ValueError:
            self.textUI.printtoTextUI(f"Invalid input. Plz enter the correct product number.")


    def hasZombiesInRoom(self):
        #check if still have zombie in this room
        return any(self.currentRoom.zombies)

    def doInventoryCommand(self):
        inventory = self.player.getInventory()
        item_name=[item.getName() for item in inventory]
        item_description = [item.getDescription() for item in inventory]
        money=self.player.show_money()
        size = self.player.inventory_size()
        heath= self.player.health

        #show the inventory infomation
        if inventory:
            items_info= [f"{item_name[i]} - {item_description[i]}" for i in range(len(inventory))]
            items_info.append("")
            items_info.append("You can choose command:")
            items_info.append("throw and item name - To throw an item")
            items_info.append("cure - To use medicine to cure yourself\n")
            items = "\n".join(items_info)
            self.textUI.printtoTextUI(f"Your inventory:\n{items}")
        else:
            self.textUI.printtoTextUI("Your inventory is empty.")
        #print infomation
        self.textUI.printtoTextUI(f"Now you have £{money} ")
        self.textUI.printtoTextUI(f"Now the column size of inventory still have {size} left.")
        self.textUI.printtoTextUI(f"Your health: {heath}\n")

    def docureCommand(self):
        medicines = [item for item in self.player.inventory if item.type == "medicine"]

        if not medicines:
            print("No medicines available.")
            return

        print("Choose a medicine:")
        for i, medicine in enumerate(medicines):
            print(f"{i}. {medicine.name} - Heal: {medicine.cure}")

        try:
            medicine_index = int(input("Enter the number of medicine you want to use:"))
            if 0 <= medicine_index < len(medicines):
                self.player.removeFromInventory(medicine)
                self.player.heal(medicine.cure)
                print(f"You used {medicine.name} successfully.\n")
            else:
                print("Invalid medicine index. Please choose a valid index.")
        except ValueError:
            print("Invalid input. Please enter a valid medicine index.")


    # attack zombies
    def attackZombie(self, zombie):

        while zombie.health > 0:
            weapons= [item for item in self.player.inventory if item.type == "weapon"]
            print("Choose a weapon:")
            for i, weapon in enumerate(weapons):
                print(f"{i}. {weapon.name} - Damage: {weapon.damage}")
            #choose weapon to attack zombie
            try:
                if len(self.player.getInventory())>0:
                    weapon_index = int(input("Enter number: "))
                    if 0 <= weapon_index < len(self.player.getInventory()):
                        #weapon = self.player.getInventory()[weapon_index]
                        weapon=weapons[weapon_index]
                        damage = weapon.use()
                        self.player.removeFromInventory(weapon)
                        reward = zombie.takeDamage(damage)

                        if reward > 0:
                            print(f"You killed the {zombie.name} and got £{reward} !\n")

                            self.currentRoom.removeZombie(zombie)
                            self.player.get_reword(reward)

                            if self.currentRoom.haszombies():
                                random_zombie = random.choice(self.currentRoom.zombies)
                                random_zombie.attackPlayer(self.player)
                                self.player_dead()
                                self.textUI.printtoTextUI("Still have zombie in this place,plz continue attack!\n")
                            else:
                                self.textUI.printtoTextUI("Now, you can take the item from this place.\n")
                                if self.currentRoom.items:
                                    items_str = ", ".join(item.name for item in self.currentRoom.items)
                                    self.textUI.printtoTextUI(f'Items in the room: {items_str}\n')
                                if self.currentRoom == self.firststreet:
                                    self.textUI.printtoTextUI(
                                        "Suggesting you go supermarket-'north' or police station-'south'.")
                                    self.textUI.printtoTextUI("Then you can go second street-'east'\n")

                                elif self.currentRoom == self.firstfloor:
                                    self.textUI.printtoTextUI("GO second floor-'upstairs' before go to the basement.")

                        else:
                            if self.currentRoom.haszombies():
                                random_zombie = random.choice(self.currentRoom.zombies)
                                random_zombie.attackPlayer(self.player)
                                self.player_dead()
                    else:
                        print("Invalid weapon index. Please choose a valid index.")
                else:
                    print(f"Sorry,you don't have any weapon now. PLZ buy it in store.")
                    break

            except ValueError:
                print("Invalid input. Please choose a valid weapon index.")
            except IndexError:
                print("SORRY. The index is out of range. PLZ input the correct index.")

    def attackZombieCommand(self):
        #when use this command
        if self.currentRoom.haszombies():
            zombies = self.currentRoom.getZombies()
            print("choose a zombie:")
            for i, zombie in enumerate(zombies):
                self.textUI.printtoTextUI(f"{i} . {zombie.name} - Health:{zombie.health}")
            try:
                zombie_index = int(input("Enter number: "))
                zombie = zombies[zombie_index]
                self.attackZombie(zombie)
            except ValueError:
                self.textUI.printtoTextUI("Invalid input. Please enter the correct index of the zombie number.")
            except IndexError:
                self.textUI.printtoTextUI("Sorry. The index is out of range. Please input the correct index.")
        else:
            self.textUI.printtoTextUI("There's no zombies in this room!! Just go to another area.")






def main():
    game = Game()
    game.play()

if __name__ == "__main__":
    main()