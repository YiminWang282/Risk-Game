"""
use store can buy some stuff by your money
"""
from Item import Item
from Player import Player


class Store:
    def __init__(self):
        self.product=[]
        self.deProdect()


    # #add product in store
    # def add_product(self,item):
    #     self.product.append(item)

    def deProdect(self):
        self.little_knife = Item("Little-knife", 3, 3, 0, 3, "weapon","the weight is 3g,have 3 points of damage value. ")
        self.big_knife = Item("Big-knife", 5, 5, 0, 5, "weapon", "the weight is 5g,have 5 points of damage value.")
        self.sword = Item("sword", 7, 7, 0, 7, "weapon", "the weight is 7g,have 7 points of damage value.")
        self.gun = Item("Gun", 10, 10, 0, 10, "weapon", "the weight is 10g,have 10 points of damage value.")
        self.little_cure = Item("little-cure", 1, 0, 5, 3, "medicine", "the weight is 1g,can cure 5 heath.")
        self.first_aid_kit = Item("first_aid_kit", 3, 0, 10, 5, "medicine", "the weight is 3g,can cure 10 heath.")

        self.product.append(self.little_knife)
        self.product.append(self.big_knife)
        self.product.append(self.sword)
        self.product.append(self.gun)
        #self.product.append(self.final_key)
        self.product.append(self.little_cure)
        self.product.append(self.first_aid_kit)

    def listProducts(self):
        #show how many products in store
        if not self.product:
            print("Sorry,it's empty!")
        else:
            print("Product list: ")
            for i,product in enumerate(self.product):
                print(f"{i}. {product.getName()} - Price:{product.getPrice()} - Info:{product.getDescription()}")

    def buyProduct(self,player,product_index):
        #buy products from store
        if not player.isInventoryFull():
            if 0<=product_index <len(self.product):
                product = self.product[product_index]
                if player.getMoney() >=product.getPrice():
                    player.substractMoney(product.getPrice())
                    player.addToInventory(product)
                    print(f"You already bought {product.getName()} for {product.getPrice()} money.\n")
                else:
                    print(f"Sorry,you don't have enough money to buy this product.\n")
            else:
                print("Invalid product index!\n")
        else:
            print("Sorry, your inventory is full, if you still want to buy then throw something.")