class Item:
    def __init__(self, name,weight,damage,cure,price,type, description):
        self.name = name
        self.weight = weight
        self.damage=damage
        self.cure = cure
        self.price = price
        self.type = type
        self.description = description

    # def defineItems(self):
    #     self.little_knife=Item("Little-knife",3,3,3,"the weight is 3g,can kill zombie_1")
    #     self.big_knife=Item("Big-knife",5,5,5,"the weight is 5g,can kill zombie_2")
    #     self.gun=Item("Gun",10,10,10,"the weight is 10g,can kill zombie_3")
    #     self.final_key=Item("final-key",10,0,10,"it can save your daughter!!")

    def getdamage(self): #got damage from weapon
        return self.damage

    def getName(self): #get name from item
        return self.name

    def getDescription(self): #show the description
        return self.description

    def getPrice(self): #show price
        return self.price

    def use(self): #when used the weapon,return the damage
        print(f"You have used {self.name}\n")
        return self.damage
