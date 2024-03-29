import tkinter as tk
from tkinter import messagebox, RIGHT, LEFT, TOP, NW, DISABLED, NORMAL, BOTTOM, ttk,SE,Label, font

import tkinter
from PIL import ImageTk, Image
from Game import Game

import datetime

#Final-version
class My_firstUI:
    def __init__(self, root, PLAYER_IMAGE):
        '''
        User initial interface
        Enter user nickname
        :param root:
        '''
        # Create the model instance ...
        self.PLAYER_IMAGE = PLAYER_IMAGE
        # PLAYER_IMAGE=0
        self.root = root
        self.root.config()
        self.userframe = tk.Frame(self.root, width=1100, height=700)
        self.userframe.pack_propagate(0)  # Prevents resizing
        self.userframe.pack()




        # Load images
        self.start_image = self.load_and_resize_image('images/welcome.jpg',width=200,height=100)
        self.image1 = self.load_and_resize_image("images/player.jpg", width=120, height=200)
        self.image2 = self.load_and_resize_image("images/player2.jpg", width=120, height=200)

        # Create Canvas for background image
        self.start = tk.Label(self.userframe, image=self.start_image, width=300, height=180)
        self.start.grid(row=0, column=0,columnspan = 2)
        self.label = tk.Label(self.userframe, text='Please enter user name', font=('Sans', '15', 'bold'))


        # Other UI elements
        self.label = tk.Label(self.userframe, text='Please enter user name', font=('Sans', '15', 'bold'))
        self.label.grid(row=1, column=0, columnspan=2)

        self.button = tk.Button(self.userframe, text='start', command=self.startcommand, font=('Sans', '15', 'bold'))
        self.button.grid(row=3, column=0, ipady=10, pady=10, columnspan=2)

        self.player_name = tk.Entry(self.userframe, text='player_name')
        self.player_name.grid(row=2, column=0, ipady=10, pady=10, columnspan=2)

        self.label_w = tk.Label(self.userframe, text='Please choose your Avatar', font=('Sans', '15', 'bold'))
        self.label_w.grid(row=4, column=0, columnspan=2)

        self.button_image1 = tk.Button(self.userframe, image=self.image1, compound=tk.BOTTOM, text='Avatar 1',
                                       command=self.Avatar1)
        self.button_image1.grid(row=5, column=0, sticky='e')  # 'e' stands for east, i.e., right

        self.button_image2 = tk.Button(self.userframe, image=self.image2, compound=tk.BOTTOM, text='Avatar 2',
                                       command=self.Avatar2)
        self.button_image2.grid(row=5, column=1, sticky='w')  # 'w' stands for west, i.e., left



    def Avatar1(self):
        # global PLAYER_IMAGE
        self.PLAYER_IMAGE = 1

    def Avatar2(self):
        # global PLAYER_IMAGE
        self.PLAYER_IMAGE = 2

    def load_and_resize_image(self, path, width, height):
        """
        can resize the image into specialized size
        :param path:
        :param width:
        :param height:
        :return:
        """
        original_image = Image.open(path)
        resized_image = original_image.resize((width, height), Image.LANCZOS)
        return ImageTk.PhotoImage(resized_image)

    def startcommand(self):
        """
            close the firstUI and start the secondUI
            Global variable: PLAYER_NAME
            Error prevention and recovery
        """
        global PLAYER_NAME
        try:
            PLAYER_NAME = self.player_name.get()
            if PLAYER_NAME.isalpha() == False:
                raise (ValueError())
        # just can input string
        except ValueError:
            messagebox.showinfo("NOTE", message="Please use String type!")
        else:
            self.userframe.destroy()
            myApp = My_secondUI(self.root, self.PLAYER_IMAGE)




class My_secondUI():
    def __init__(self, root, PLAYER_IMAGE):
        '''
        The main interface of the game
        :param root:
        '''
        # Create the model instance ...
        self.PLAYER_IMAGE = PLAYER_IMAGE
        self.game = Game()
        self.items = self.game.creatItems()
        self.game.player.addToInventory(self.game.little_knife)
        self.game.player.addToInventory(self.game.little_cure)

        self.res = False
        self.root = root

        self.custom_font = font.Font(family="Helvetica", size=12,weight="bold")

        self.nowroom = 'saferoom'



        # Create the GUI
        # add menubar
        menubar = tk.Menu()
        menubar.add_command(label="Quit", command=root.destroy)
        root.config(menu=menubar)
        menubar.add_command(label="About", command=self.about)
        root.config(menu=menubar)

        # the frame of game
        self.frame1 = tk.Frame(root, width=850, height=640, borderwidth=2)
        self.frame1.pack_propagate(0)  # Prevents resizing
        self.frame1.pack(side=LEFT)#main frame

        # Add the initialization for self.current_scene_canvas here
        self.current_scene_canvas = tk.Canvas(self.frame1, width=800, height=400)
        self.frame2 = tk.Frame(root, width=250, height=650, borderwidth=2)
        self.frame2.pack_propagate(0)  # Prevents resizing
        self.frame2.pack(side=RIGHT)
        # add frame into frame2
        self.frame3 = tk.Frame(self.frame2, width=250, height=350, borderwidth=2)
        self.frame3.pack_propagate(0)  # Prevents resizing
        self.frame3.pack(side=TOP)
        self.frame4 = tk.Frame(self.frame2, width=250, height=350, borderwidth=2)
        self.frame4.pack_propagate(0)  # Prevents resizing
        self.frame4.pack(side=TOP)
        self.frame5 = tk.Frame(self.frame2, width=250, height=350, borderwidth=2)
        self.frame5.pack_propagate(0)  # Prevents resizing
        self.frame5.pack(side=TOP)

        #add frame6 into frame1
        self.frame6 = tk.Frame(self.frame1,width=400,height=200,borderwidth=3)
        self.frame6.pack_propagate(0)
        self.frame6.place(x=400,y=450)


        #configure of 3,4
        self.frame3.columnconfigure(0, pad=10)
        for i in range(6):
            self.frame3.rowconfigure(i, pad=10)
        for i in range(2):
            self.frame4.columnconfigure(i, pad=10)
        for i in range(4):
            self.frame4.rowconfigure(i, pad=10)

        for i in range(4):
            self.frame6.columnconfigure(i,pad=10)


        # get images
        # global PLAYER_IMAGE
        if self.PLAYER_IMAGE == 2:
            self.character = self.load_and_resize_image("images/player2.jpg",width=50,height=80)
        else:
            self.character = self.load_and_resize_image("images/player.jpg",width=50,height=80)





        # Load images
        self.east = self.load_and_resize_image("images/east.png", width=50, height=50)
        self.west = self.load_and_resize_image("images/west.png", width=50, height=50)
        self.south = self.load_and_resize_image("images/south.png", width=50, height=50)
        self.north = self.load_and_resize_image("images/north.png", width=50, height=50)
        self.weapon = self.load_and_resize_image("images/axe.png", width=55, height=55)
        self.money = self.load_and_resize_image("images/coin.png", width=50, height=50)
        self.heart = self.load_and_resize_image("images/heart.png", width=50, height=50)
        self.stair = self.load_and_resize_image("images/wooden_stairs-ns.png", width=50, height=50)
        self.key = self.load_and_resize_image("images/key.png",width=50,height=50)
        self.attack = self.load_and_resize_image("images/attack.png",width=80,height=80)
        self.cure = self.load_and_resize_image("images/cure.png",width=80,height=80)
        self.pick = self.load_and_resize_image("images/pick.png",width=80,height=80)
        self.store = self.load_and_resize_image("images/store.png",width=80,height=80)
        self.daughter = self.load_and_resize_image("images/daughter.png",width=50,height=50)
        self.helicopter = self.load_and_resize_image("images/helicopter.png",width=200,height=100)


        #the senery background
        self.saferoom_bg=self.load_and_resize_image("images/saferoom.png",width=850,height=400)
        self.firststreet_bg=self.load_and_resize_image("images/firststreet.jpg",width=850,height=400)
        self.policestation_bg=self.load_and_resize_image("images/policestation.jpg",width=850,height=400)
        self.supermarket_bg=self.load_and_resize_image("images/supermarket.jpg",width=850,height=400)
        self.secondStreet_bg=self.load_and_resize_image("images/secondstreet.jpg",width=850,height=400)
        self.campus_bg=self.load_and_resize_image("images/campus.jpg",width=850,height=400)
        self.firstfloor_bg=self.load_and_resize_image("images/firstfloor.jpg",width=850,height=400)
        self.basement_bg=self.load_and_resize_image("images/basement.png",width=850,height=400)
        self.secondfloor_bg=self.load_and_resize_image("images/secondfloor.png",width=850,height=400)
        self.rooftop_bg=self.load_and_resize_image("images/rooftop.png",width=850,height=400)

        # add button
        options = ['background introduction', 'button introduction','keyboard control']  # List with all options
        self.v = tk.StringVar(self.frame3)
        self.v.set("help")  # default value
        self.v.trace("w", self.help)
        self.w = tk.OptionMenu(self.frame3, self.v, *options)
        self.w.grid(row=0, column=0)
        self.button_bag = tk.Button(self.frame3, text="My beg", command=lambda: self.usebag())
        self.button_bag.grid(row=1, column=0)
        self.button_weapon = tk.Button(self.frame3, text="weapon", image=self.weapon, compound=tkinter.BOTTOM,
                                       command=lambda: self.checkweapon())
        self.button_weapon.grid(row=4, column=0)

        # choose direction
        self.button_north = tk.Button(self.frame4, text="north", image=self.north, compound=tkinter.BOTTOM,
                                      command=lambda: self.North())
        self.button_north.grid(row=0, column=0)
        self.button_south = tk.Button(self.frame4, text="south", image=self.south, compound=tkinter.BOTTOM,
                                      command=lambda: self.South())
        self.button_south.grid(row=0, column=1)
        self.button_west = tk.Button(self.frame4, text="west", image=self.west, compound=tkinter.BOTTOM,
                                     command=lambda: self.West())
        self.button_west.grid(row=1, column=0)
        self.button_east = tk.Button(self.frame4, text="east", image=self.east, compound=tkinter.BOTTOM,
                                     command=lambda: self.East())
        self.button_east.grid(row=1, column=1)


        self.button_up = tk.Button(self.frame4, text="upstairs", image=self.stair, compound=tkinter.BOTTOM,
                                   command=lambda: self.Up())
        self.button_up.grid(row=2, column=0)
        self.button_down = tk.Button(self.frame4, text="downstairs", image=self.stair, compound=tkinter.BOTTOM,
                                     command=lambda: self.Down())
        self.button_down.grid(row=2, column=1)

        self.attack_button = tk.Button(self.frame6,text="ATTACK",image=self.attack,compound=tkinter.BOTTOM,command= lambda :self.attack_command())
        self.attack_button.grid(row =0 ,column =0)
        self.cure_button = tk.Button(self.frame6,text="CURE",image=self.cure,compound=tkinter.BOTTOM,command=lambda :self.cure_command())
        self.cure_button.grid(row=0,column=1)
        self.pick_button = tk.Button(self.frame6,text="PICK",image=self.pick,compound=tkinter.BOTTOM,command=lambda :self.pick_command())
        self.pick_button.grid(row=0,column=2)
        self.store_button = tk.Button(self.frame6,text="STORE",image=self.store,compound=tkinter.BOTTOM,command=lambda :self.store_command())
        self.store_button.grid(row=0,column=3)



        # LABEL
        self.label_HP = tk.Label(self.frame5, text="Your life: " + str(self.game.player.health), image=self.heart,
                                 compound=tkinter.LEFT)
        self.label_HP.pack(side=TOP)
        self.label_COIN = tk.Label(self.frame5, text="Your money: " + str(self.game.player.money), image=self.money,
                                   compound=tkinter.LEFT)
        self.label_COIN.pack(side=TOP)
        self.label_KEY = tk.Label(self.frame5, text="Final key: " + str(self.game.player.haskey("final-key")),
                                  image=self.key,
                                  compound=tkinter.LEFT)
        self.label_KEY.pack(side=TOP)

        #start room
        self.saferoom()

        #save zombie images
        self.zombie_images = {}

    def update_coin_label(self):
        """
        renew the condition of player
        :return:
        """
        self.label_COIN.config(text="Your money: " + str(self.game.player.money))
        self.label_HP.config(text="Your life: " +str(self.game.player.health))
        self.label_KEY.config(text="Final key: "+str(self.game.player.haskey("final-key")))


    def close_previous_scene(self):
        """
        Forget the canvas if it exists and is currently packed
        :return:
        """
        if self.current_scene_canvas and self.current_scene_canvas.winfo_ismapped():
            self.current_scene_canvas.pack_forget()
            # Clear all items on the canvas
            self.current_scene_canvas.delete("all")



    def button_control(self):
        """
        control the button in specialized scenery
        :return:
        """
        if self.game.player.health == self.game.player.health_max:
            self.cure_button.configure(state=DISABLED)
        else:
            has_medicine = any(item.type == "medicine" for item in self.game.player.inventory)
            self.cure_button.configure(state=NORMAL if has_medicine else DISABLED)

        if self.game.currentRoom.haszombies():
            self.attack_button.configure(state=NORMAL)
            self.pick_button.configure(state=DISABLED)
        else:
            self.attack_button.configure(state=DISABLED)
            if not self.game.currentRoom.items:
                self.pick_button.configure(state=DISABLED)
            else:
                self.pick_button.configure(state=NORMAL)

    def saferoom(self):
        """
        saferoom for start
        :return:
        """
        self.mylog('in the safe room')
        # Close the previous scene
        self.close_previous_scene()

        # Design saferoom
        self.button_up.configure(state=DISABLED)
        self.button_east.configure(state=NORMAL)
        self.button_west.configure(state=DISABLED)
        self.button_north.configure(state=DISABLED)
        self.button_south.configure(state=DISABLED)
        self.button_down.configure(state=DISABLED)
        self.button_control()

        # Info label
        self.location = tk.Label(self.frame1, text='Hi, ' + str(PLAYER_NAME) + " Your location: Saferoom.",font=self.custom_font)
        self.location.place(x=0, y=0, width=300, height=20)
        if hasattr(self, 'label_text'):
            self.label_text.destroy()
        self.label_text = tk.Label(self.frame1, text="This is saferoom, you can go east.",font=self.custom_font)
        self.label_text.place(x=0, y=440, width=300, height=30)

        # Create and configure canvas
        self.current_scene_canvas.config(width=800, height=400)
        self.saferoom_image = self.current_scene_canvas.create_image(20, 30, anchor=NW, image=self.saferoom_bg)

        # Create man in canvas
        self.people_x = 100
        self.people_y = 280
        self.man = self.current_scene_canvas.create_image(self.people_x, self.people_y, anchor=NW, image=self.character)

        # load zombie into room
        zombies_x = self.people_x + 400
        zombies_y = self.people_y
        if not self.game.currentRoom.haszombies():
            self.load_items_in_room(zombies_x,zombies_y)

        # Bind keyboard events to corresponding methods
        self.root.bind('<KeyPress-a>', self.move_left)
        self.root.bind('<KeyPress-d>', self.move_right)

        # Pack the canvas
        self.current_scene_canvas.pack()

    def first_street(self):
        """
        first street
        :return:
        """
        self.mylog('in the first street')
        # Close the previous scene
        self.close_previous_scene()

        #control the condition of getting next room
        self.button_up.configure(state=DISABLED)
        if not (self.game.supermarket.haszombies() and self.game.policestation.haszombies()):
            self.button_east.configure(state=NORMAL)
        else:
            self.button_east.configure(state=DISABLED)
        if not self.game.currentRoom.haszombies():
            self.button_south.configure(state=NORMAL)
            self.button_north.configure(state=NORMAL)
        else:
            self.button_south.configure(state=DISABLED)
            self.button_north.configure(state=DISABLED)
        self.button_west.configure(state=NORMAL)

        self.button_down.configure(state=DISABLED)
        self.button_control()


        # Destroy the previous label_text, if it exists
        self.location = tk.Label(self.frame1, text='Hi, ' + str(PLAYER_NAME) + " Your location: first street.",font=self.custom_font)
        self.location.place(x=0, y=0, width=300, height=20)
        if hasattr(self, 'label_text'):
            self.label_text.destroy()

        self.label_text = tk.Label(self.frame1, text="This is first street,\n"
                                                     "you should clear the zombies\n"
                                                     "in the supermarket and policestation,\n"
                                                     "then you can go to the second street.",font=self.custom_font)
        self.label_text.place(x=0, y=440, width=300, height=80)

        # Create and configure canvas
        self.current_scene_canvas.config(width=800, height=400)
        self.firststreet_img = self.current_scene_canvas.create_image(20, 30, anchor=NW, image=self.firststreet_bg)

        # Create man in canvas
        self.people_x = 100
        self.people_y = 300
        self.man = self.current_scene_canvas.create_image(self.people_x, self.people_y, anchor=NW, image=self.character)

        # load zombies
        zombies_x = self.people_x + 400
        zombies_y = self.people_y
        self.load_zombie(zombies_x, zombies_y)

        if not self.game.currentRoom.haszombies():
            self.load_items_in_room(zombies_x,zombies_y)

        # Bind keyboard events to corresponding methods
        self.root.bind('<KeyPress-a>', self.move_left)
        self.root.bind('<KeyPress-d>', self.move_right)

        # Pack the canvas
        self.current_scene_canvas.pack()


    def supermarket(self):
        """
        supermarket
        :return:
        """
        self.mylog('in the supermarket')
        self.button_up.configure(state=DISABLED)
        self.button_east.configure(state=DISABLED)
        self.button_west.configure(state=DISABLED)
        self.button_north.configure(state=NORMAL)
        self.button_south.configure(state=DISABLED)
        self.button_down.configure(state=DISABLED)
        self.button_control()

        # Close the previous scene
        self.close_previous_scene()


        # Info label
        self.location = tk.Label(self.frame1, text='Hi, ' + str(PLAYER_NAME) + " Your location: supermarket.",font=self.custom_font)
        self.location.place(x=0, y=0, width=300, height=20)

        if hasattr(self, 'label_text'):
            self.label_text.destroy()

        self.label_text = tk.Label(self.frame1, text="Come on!!!",font=self.custom_font)
        self.label_text.place(x=0, y=440, width=300, height=30)

        # Create and configure canvas
        self.current_scene_canvas.config(width=800, height=400)
        self.supermarket_img = self.current_scene_canvas.create_image(20, 30, anchor=NW, image=self.supermarket_bg)

        # Create man in canvas
        self.people_x = 100
        self.people_y = 280
        self.man = self.current_scene_canvas.create_image(self.people_x, self.people_y, anchor=NW, image=self.character)

        #load zombies
        zombies_x = self.people_x + 400
        zombies_y = self.people_y
        self.load_zombie(zombies_x, zombies_y)

        if not self.game.currentRoom.haszombies():
            self.load_items_in_room(zombies_x,zombies_y)

        # Bind keyboard events to corresponding methods
        self.root.bind('<KeyPress-a>', self.move_left)
        self.root.bind('<KeyPress-d>', self.move_right)

        # Pack the canvas
        self.current_scene_canvas.pack()

    def policestation(self):
        """
        police station
        :return:
        """
        self.mylog('in the policestation')
        self.button_up.configure(state=DISABLED)
        self.button_east.configure(state=DISABLED)
        self.button_west.configure(state=DISABLED)
        self.button_north.configure(state=DISABLED)
        self.button_south.configure(state=NORMAL)
        self.button_down.configure(state=DISABLED)
        self.button_control()

        # Close the previous scene
        self.close_previous_scene()

        # Info label
        self.location = tk.Label(self.frame1, text='Hi, ' + str(PLAYER_NAME) + " Your location: police station.",font=self.custom_font)
        self.location.place(x=0, y=0, width=300, height=20)

        if hasattr(self, 'label_text'):
            self.label_text.destroy()
        self.label_text = tk.Label(self.frame1, text="DON'T forget pick up the supplies.",font=self.custom_font)
        self.label_text.place(x=0, y=440, width=300, height=100)

        # Create and configure canvas
        self.current_scene_canvas.config(width=800, height=400)
        self.policestation_img = self.current_scene_canvas.create_image(20, 30, anchor=NW, image=self.policestation_bg)

        # Create man in canvas
        self.people_x = 100
        self.people_y = 280
        self.man = self.current_scene_canvas.create_image(self.people_x, self.people_y, anchor=NW, image=self.character)

        # load zombies
        zombies_x = self.people_x + 400
        zombies_y = self.people_y
        self.load_zombie(zombies_x, zombies_y)

        if not self.game.currentRoom.haszombies():
            self.load_items_in_room(zombies_x,zombies_y)

        # Bind keyboard events to corresponding methods
        self.root.bind('<KeyPress-a>', self.move_left)
        self.root.bind('<KeyPress-d>', self.move_right)

        # Pack the canvas
        self.current_scene_canvas.pack()


    def second_street(self):
        """
        second street
        :return:
        """
        self.mylog('in the second street')
        self.button_up.configure(state=DISABLED)
        if not self.game.currentRoom.haszombies():
            self.button_east.configure(state=NORMAL)
        else:
            self.button_east.configure(state=DISABLED)

        self.button_west.configure(state=NORMAL)
        self.button_north.configure(state=DISABLED)
        self.button_south.configure(state=DISABLED)
        self.button_down.configure(state=DISABLED)
        self.button_control()

        # Close the previous scene
        self.close_previous_scene()

        self.location = tk.Label(self.frame1, text='Hi, ' + str(PLAYER_NAME) + " Your location: second street.",font=self.custom_font)
        self.location.place(x=0, y=0, width=300, height=20)

        # Destroy the previous label_text, if it exists
        if hasattr(self, 'label_text'):
            self.label_text.destroy()

        self.label_text = tk.Label(self.frame1, text="GO,GO,GO!",font=self.custom_font)
        self.label_text.place(x=0, y=440, width=300, height=80)

        # Create and configure canvas
        self.current_scene_canvas.config(width=800, height=400)
        self.secondStreet_img = self.current_scene_canvas.create_image(20, 30, anchor=NW, image=self.secondStreet_bg)

        self.people_x = 100
        self.people_y = 300
        # Create man in canvas
        self.man = self.current_scene_canvas.create_image(self.people_x, self.people_y, anchor=NW, image=self.character)

        #load zombies
        zombies_x = self.people_x + 400
        zombies_y = self.people_y
        self.load_zombie(zombies_x, zombies_y)

        if not self.game.currentRoom.haszombies():
            self.load_items_in_room(zombies_x,zombies_y)

        # Bind keyboard events to corresponding methods
        self.root.bind('<KeyPress-a>', self.move_left)
        self.root.bind('<KeyPress-d>', self.move_right)

        # Pack the canvas
        self.current_scene_canvas.pack()


    def campus(self):
        """
        campus
        :return:
        """
        self.mylog('in the campus')
        self.button_up.configure(state=DISABLED)
        self.button_east.configure(state=DISABLED)
        self.button_west.configure(state=NORMAL)
        self.button_north.configure(state=DISABLED)
        if not self.game.currentRoom.haszombies():
            self.button_south.configure(state=NORMAL)
        else:
            self.button_south.configure(state=DISABLED)
        self.button_down.configure(state=DISABLED)
        self.button_control()

        # Close the previous scene
        self.close_previous_scene()

        self.location = tk.Label(self.frame1, text='Hi, ' + str(PLAYER_NAME) + " Your location: campus.",font=self.custom_font)
        self.location.place(x=0, y=0, width=300, height=20)

        # Destroy the previous label_text, if it exists
        if hasattr(self, 'label_text'):
            self.label_text.destroy()

        self.label_text = tk.Label(self.frame1, text="This is school campus.",font=self.custom_font)
        self.label_text.place(x=0, y=440, width=300, height=80)

        # Create and configure canvas
        self.current_scene_canvas.config(width=800, height=400)
        self.campus_img = self.current_scene_canvas.create_image(20, 30, anchor=NW, image=self.campus_bg)

        # Create man in canvas
        self.people_x = 100
        self.people_y = 300
        self.man = self.current_scene_canvas.create_image(self.people_x, self.people_y, anchor=NW, image=self.character)

        #load zombies
        zombies_x = self.people_x + 400
        zombies_y = self.people_y
        self.load_zombie(zombies_x, zombies_y)
        if not self.game.currentRoom.haszombies():
            self.load_items_in_room(zombies_x,zombies_y)

        # Bind keyboard events to corresponding methods
        self.root.bind('<KeyPress-a>', self.move_left)
        self.root.bind('<KeyPress-d>', self.move_right)

        # Pack the canvas
        self.current_scene_canvas.pack()

    def firstfloor(self):
        """
        first floor
        :return:
        """
        self.mylog('in the first floor')

        #control button
        self.button_east.configure(state=DISABLED)
        self.button_west.configure(state=DISABLED)
        self.button_north.configure(state=NORMAL)
        self.button_south.configure(state=DISABLED)
        if not self.game.currentRoom.haszombies():
            self.button_up.configure(state=NORMAL)
        else:
            self.button_up.configure(state=DISABLED)
        if not self.game.secondfloor.haszombies():
            self.button_down.configure(state=NORMAL)
        else:
            self.button_down.configure(state=DISABLED)

        self.button_control()

        # Close the previous scene
        self.close_previous_scene()

        self.location = tk.Label(self.frame1, text='Hi, ' + str(PLAYER_NAME) + " Your location: first floor.",font=self.custom_font)
        self.location.place(x=0, y=0, width=300, height=20)

        # Destroy the previous label_text, if it exists
        if hasattr(self, 'label_text'):
            self.label_text.destroy()
        self.label_text = tk.Label(self.frame1, text="Go second floor first.\n"
                                                     "Then you can go to the basement.",font=self.custom_font)
        self.label_text.place(x=0, y=440, width=300, height=80)

        # Create and configure canvas
        self.current_scene_canvas.config(width=800, height=400)
        self.firstfloor_img = self.current_scene_canvas.create_image(20, 30, anchor=NW, image=self.firstfloor_bg)

        # Create man in canvas
        self.people_x = 100
        self.people_y = 300
        self.man = self.current_scene_canvas.create_image(self.people_x, self.people_y, anchor=NW, image=self.character)

        # load zombies
        zombies_x = self.people_x + 400
        zombies_y = self.people_y
        self.load_zombie(zombies_x, zombies_y)

        if not self.game.currentRoom.haszombies():
            self.load_items_in_room(zombies_x,zombies_y)

        # Bind keyboard events to corresponding methods
        self.root.bind('<KeyPress-a>', self.move_left)
        self.root.bind('<KeyPress-d>', self.move_right)

        # Pack the canvas
        self.current_scene_canvas.pack()


    def secondfloor(self):
        """
        second floor
        :return:
        """
        self.mylog('in the second floor')

        if not self.game.player.haskey("final-key"):
            self.button_up.configure(state=DISABLED)
        else:
            self.button_up.configure(state=NORMAL)
        self.button_east.configure(state=DISABLED)
        self.button_west.configure(state=DISABLED)
        self.button_north.configure(state=DISABLED)
        self.button_south.configure(state=DISABLED)
        self.button_down.configure(state=NORMAL)
        self.button_control()

        # Close the previous scene
        self.close_previous_scene()

        # Info label
        self.location = tk.Label(self.frame1, text='Hi, ' + str(PLAYER_NAME) + " Your location: second floor.",font=self.custom_font)
        self.location.place(x=0, y=0, width=300, height=20)

        if hasattr(self, 'label_text'):
            self.label_text.destroy()
        self.label_text = tk.Label(self.frame1, text="After defeated all the zombies here.\n"
                                                     "You should go to the basement.\n"
                                                     "Pick the final-key,\n"
                                                     "and save your daughter.\n"
                                                     "Then go to the rooftop.",font=self.custom_font)
        self.label_text.place(x=0, y=440, width=300, height=100)

        # Create and configure canvas
        self.current_scene_canvas.config(width=800, height=400)
        self.secondfloor_img = self.current_scene_canvas.create_image(20, 30, anchor=NW, image=self.secondfloor_bg)

        # Create man in canvas
        self.people_x = 100
        self.people_y = 280
        self.man = self.current_scene_canvas.create_image(self.people_x, self.people_y, anchor=NW, image=self.character)

        # load zombies
        zombies_x = self.people_x + 400
        zombies_y = self.people_y
        self.load_zombie(zombies_x, zombies_y)

        if not self.game.currentRoom.haszombies():
            self.load_items_in_room(zombies_x,zombies_y)

        # Bind keyboard events to corresponding methods
        self.root.bind('<KeyPress-a>', self.move_left)
        self.root.bind('<KeyPress-d>', self.move_right)

        # Pack the canvas
        self.current_scene_canvas.pack()



    def basement(self):
        """
        basement
        :return:
        """
        self.mylog('in the basement')
        self.button_up.configure(state=NORMAL)
        self.button_east.configure(state=DISABLED)
        self.button_west.configure(state=DISABLED)
        self.button_north.configure(state=DISABLED)
        self.button_south.configure(state=DISABLED)
        self.button_down.configure(state=DISABLED)
        self.button_control()

        # Close the previous scene
        self.close_previous_scene()

        # Info label
        self.location = tk.Label(self.frame1, text='Hi, ' + str(PLAYER_NAME) + " Your location: basement.",font=self.custom_font)
        self.location.place(x=0, y=0, width=300, height=20)

        if hasattr(self, 'label_text'):
            self.label_text.destroy()
        self.label_text = tk.Label(self.frame1, text="Your daughter is here.\n"
                                                     "And pick up the final-key!",font=self.custom_font)
        self.label_text.place(x=0, y=440, width=300, height=100)

        # Create and configure canvas
        self.current_scene_canvas.config(width=800, height=400)
        self.basement_img = self.current_scene_canvas.create_image(20, 30, anchor=NW, image=self.basement_bg)

        # Create man in canvas
        self.people_x = 100
        self.people_y = 300
        self.man = self.current_scene_canvas.create_image(self.people_x, self.people_y, anchor=NW, image=self.character)

        # check if have final-key
        if not self.game.player.haskey("final-key"):
            self.crying = self.current_scene_canvas.create_image(600,330,anchor =NW ,image=self.daughter)

        # load zombies
        zombies_x = self.people_x + 400
        zombies_y = self.people_y
        self.load_zombie(zombies_x, zombies_y)

        if not self.game.currentRoom.haszombies():
            self.load_items_in_room(zombies_x,zombies_y)

        # Bind keyboard events to corresponding methods
        self.root.bind('<KeyPress-a>', self.move_left)
        self.root.bind('<KeyPress-d>', self.move_right)

        # Pack the canvas
        self.current_scene_canvas.pack()


    def rooftop(self):
        """
        rooftop
        :return:
        """
        self.mylog('in the roof top')
        self.button_up.configure(state=DISABLED)
        self.button_east.configure(state=DISABLED)
        self.button_west.configure(state=DISABLED)
        self.button_north.configure(state=DISABLED)
        self.button_south.configure(state=DISABLED)
        self.button_down.configure(state=DISABLED)
        self.button_control()

        # Close the previous scene
        self.close_previous_scene()

        # Info label
        self.location = tk.Label(self.frame1, text='Hi, ' + str(PLAYER_NAME) + " Your location: roof top.",font=self.custom_font)
        self.location.place(x=0, y=0, width=300, height=20)

        if hasattr(self, 'label_text'):
            self.label_text.destroy()
        self.label_text = tk.Label(self.frame1, text="Use 'A' go left,'D' go right,\n"
                                                     "Go to the helicopter,\n"
                                                     "and run away from this city!",font=self.custom_font)
        self.label_text.place(x=0, y=440, width=300, height=100)

        # Create and configure canvas
        self.current_scene_canvas.config(width=800, height=400)
        self.rooftop_img = self.current_scene_canvas.create_image(20, 30, anchor=NW, image=self.rooftop_bg)

        # Create man in canvas
        self.people_x = 100
        self.people_y = 280
        self.man = self.current_scene_canvas.create_image(self.people_x, self.people_y, anchor=NW, image=self.character)

        # add the condition of succeed game
        self.escape_x = 500
        self.escape_y =250
        self.escape = self.current_scene_canvas.create_image(self.escape_x,self.escape_y,anchor=NW, image=self.helicopter)
        # Bind keyboard events to corresponding methods
        self.root.bind('<KeyPress-a>', self.move_left)
        self.root.bind('<KeyPress-d>', self.move_right)

        # Pack the canvas
        self.current_scene_canvas.pack()

    def move_left(self, event):
        """
        control the player move left
        :param event:
        :return:
        """
        # move left
        new_x = self.people_x - 10
        if 70 <= new_x <= 800 - 100:  # Canvas宽度是800，人物图片宽度是55
            self.people_x = new_x
            self.current_scene_canvas.coords(self.man, self.people_x, self.people_y)

        #if touched the helicopter
        if self.game.currentRoom==self.game.rooftop:
            if self.people_x==self.escape_x:
                self.mylog('You win ')
                messagebox.showinfo("Congratulations", "You escaped from this city!!!")
                self.frame1.destroy()
                self.frame2.destroy()
                myApp = My_thirdUI(self.root)

    def move_right(self, event):
        """
        control the player move right
        :param event:
        :return:
        """
        new_x = self.people_x + 10
        if 70 <= new_x <= 800 - 100:  # Canvas宽度是800，人物图片宽度是55
            self.people_x = new_x
            self.current_scene_canvas.coords(self.man, self.people_x, self.people_y)
        # if touched the helicopter
        if self.game.currentRoom==self.game.rooftop:
            if self.people_x == self.escape_x:
                self.mylog('You win ')
                messagebox.showinfo("Congratulations", "You escaped from this city!!!")
                self.frame1.destroy()
                self.frame2.destroy()
                myApp = My_thirdUI(self.root)


    def load_and_resize_image(self, path, width, height):
        """
        resize the image be loaded
        :param path:
        :param width:
        :param height:
        :return:
        """
        original_image = Image.open(path)
        resized_image = original_image.resize((width, height), Image.LANCZOS)
        return ImageTk.PhotoImage(resized_image)


    def usebag(self):
        '''
        Use backpack
        If using the wrong item causes the health to be less than 0
        The game is over
        You can use the props again when it is equal to 0
        :return:
        '''
        self.mylog('use bag')
        items = [item for item in self.game.player.inventory]
        items_counts = {}
        for item in items:
            item_name = item.name
            item_quantity = 1
            # If the weapon name is not in the dictionary, add it with the quantity as the value
            if item_name not in items_counts:
                items_counts[item_name] = item_quantity
            else:
                # If the weapon name is already in the dictionary, increment the quantity
                items_counts[item_name] += item_quantity
                # Create a new window for displaying weapons
        items_window = tk.Toplevel(self.root)
        items_window.title("My backpack(check/drop)")
        items_window.geometry("600x400")

        # Ensure 'My backpack' window stays in front of the main window
        items_window.grab_set()

        # Create a frame to hold items information
        weapon_frame = ttk.Frame(items_window)
        weapon_frame.grid(row=0, column=0, padx=10, pady=10)

        messagebox.showinfo("Beg size", f"Your beg size is 50g"
                                        f"\nNow empty size is{self.game.player.max_inventory_size}g")
        # Iterate through weapon_counts and display information
        for item_name, quantity in items_counts.items():
            label_text = f"{item_name} - Quantity: {quantity}"

            # Assuming you have a function to get the image path based on weapon_name
            image_path = self.get_items_image_path(item_name)

            # Load and resize the weapon image
            item_image = Image.open(image_path)
            item_image = item_image.resize((50, 50), Image.LANCZOS)  # Adjust size as needed
            item_image = ImageTk.PhotoImage(item_image)

            # Create a button with the weapon information and image
            weapon_button = ttk.Button(weapon_frame, text=label_text, image=item_image, compound=tk.LEFT,
                                       command=lambda name=item_name: self.drop_item(name, items_window))
            weapon_button.image = item_image  # Keep a reference to prevent image from being garbage collected
            weapon_button.pack(pady=5)


    def drop_item(self,item_name,items_window):
        """
        drop item
        :param item_name:
        :param items_window:
        :return:
        """
        for item in self.game.player.inventory:
            if item_name == item.name:
                self.game.player.removeFromInventory(item)
                break
        messagebox.showinfo("Drop item",f"You already drop {item_name}"
                                        f"\nNow you beg size is {self.game.player.max_inventory_size}g")
        items_window.destroy()


    def checkweapon(self):
        '''Check weapon'''
        self.mylog('Check weapon')
        weapons = [item for item in self.game.player.inventory if item.type == "weapon"]
        #print(weapons)
        # Create a dictionary to store weapon names as keys and their quantities as values
        weapon_counts = {}

        # Count the quantities of each weapon
        for weapon in weapons:
            weapon_name = weapon.name
            weapon_quantity = 1

            # If the weapon name is not in the dictionary, add it with the quantity as the value
            if weapon_name not in weapon_counts:
                weapon_counts[weapon_name] = weapon_quantity
            else:
                # If the weapon name is already in the dictionary, increment the quantity
                weapon_counts[weapon_name] += weapon_quantity

        # Create a new window for displaying weapons
        weapon_window = tk.Toplevel(self.root)
        weapon_window.title("Weapons Inventory")
        weapon_window.geometry("600x400")

        # Create a frame to hold weapon information
        weapon_frame = ttk.Frame(weapon_window)
        weapon_frame.grid(row=0, column=0, padx=10, pady=10)

        # Iterate through weapon_counts and display information
        for weapon_name, quantity in weapon_counts.items():
            label_text = f"{weapon_name} - Quantity: {quantity}"

            # Assuming you have a function to get the image path based on weapon_name
            image_path = self.get_items_image_path(weapon_name)

            # Load and resize the weapon image
            weapon_image = Image.open(image_path)
            weapon_image = weapon_image.resize((50, 50), Image.LANCZOS)  # Adjust size as needed
            weapon_image = ImageTk.PhotoImage(weapon_image)

            # Create a label to display weapon information and image
            weapon_label = ttk.Label(weapon_frame, text=label_text, image=weapon_image, compound=tk.LEFT)
            weapon_label.image = weapon_image  # Keep a reference to prevent image from being garbage collected
            weapon_label.pack(pady=5)



    def choose_weapon(self):
        '''Check weapon'''
        weapons = [item for item in self.game.player.inventory if item.type == "weapon"]
        # print(weapons)
        # Create a dictionary to store weapon names as keys and their quantities as values
        weapon_counts = {}

        # Count the quantities of each weapon
        for weapon in weapons:
            weapon_name = weapon.name
            weapon_quantity = 1

            # If the weapon name is not in the dictionary, add it with the quantity as the value
            if weapon_name not in weapon_counts:
                weapon_counts[weapon_name] = weapon_quantity
            else:
                # If the weapon name is already in the dictionary, increment the quantity
                weapon_counts[weapon_name] += weapon_quantity

        # Create a new window for displaying weapons
        weapon_window = tk.Toplevel(self.root)
        weapon_window.title("Choose weapon")
        weapon_window.geometry("600x400")

        # Create a frame to hold weapon information
        weapon_frame = ttk.Frame(weapon_window)
        weapon_frame.grid(row=0, column=0, padx=10, pady=10)

        # Iterate through weapon_counts and display information
        for weapon_name, quantity in weapon_counts.items():
            label_text = f"{weapon_name} - Quantity: {quantity}"

            # Assuming you have a function to get the image path based on weapon_name
            image_path = self.get_items_image_path(weapon_name)

            # Load and resize the weapon image
            weapon_image = Image.open(image_path)
            weapon_image = weapon_image.resize((50, 50), Image.LANCZOS)  # Adjust size as needed
            weapon_image = ImageTk.PhotoImage(weapon_image)

            # Create a button with the weapon information and image
            weapon_button = ttk.Button(weapon_frame, text=label_text, image=weapon_image, compound=tk.LEFT,
                                       command=lambda name=weapon_name: self.select_weapon(name,weapon_window))
            weapon_button.image = weapon_image  # Keep a reference to prevent image from being garbage collected
            weapon_button.pack(pady=5)




    def select_weapon(self, weapon_name,weapon_window):
        """
        choose the weapon you want to use
        :param weapon_name:
        :param weapon_window:
        :return:
        """
        # record the name of selected weapon
        self.selected_weapon_name = weapon_name
        for item in self.game.player.inventory:
            if item.type == "weapon" and item.name == weapon_name:
                self.game.player.removeFromInventory(item)
                break
        messagebox.showinfo("NOTE", message=f"You selected {self.selected_weapon_name}.")
        weapon_window.destroy()
        self.choose_zombie()



    def choose_zombie(self):
        """
        choose the zombie you want to attack
        :return:
        """
        if self.game.currentRoom.haszombies():
            # Create a new window for displaying weapons
            zombie_window = tk.Toplevel(self.root)
            zombie_window.title("Choose zombie for attack")
            zombie_window.geometry("350x350")

            # Create a frame to hold weapon information
            zombie_frame = ttk.Frame(zombie_window)
            zombie_frame.grid(row=0, column=0, padx=10, pady=10)
            zombies = self.game.currentRoom.getZombies()

            for zombie in zombies:
                #print(zombie.name)
                zombie_path = self.get_zombies_image_path(zombie.name)
                #print(zombie_path)
                zombie_img = Image.open(zombie_path)
                zombie_img = zombie_img.resize((50, 80), Image.LANCZOS)
                zombie_image = ImageTk.PhotoImage(zombie_img)
                label_text=zombie.name

                # Create a button with the weapon information and image
                zombie_button = ttk.Button(zombie_frame, text=label_text, image=zombie_image, compound=tk.LEFT,
                                           command=lambda name=label_text: self.attack_selected_zombie(name,zombie_window))
                zombie_button.image = zombie_image  # Keep a reference to prevent image from being garbage collected
                zombie_button.pack(pady=5)

    def attack_selected_zombie(self, zombie_name,zombie_window):
        '''attack the zombie you chose'''
        if self.selected_weapon_name:
            selected_zombie = self.get_zombie_object(zombie_name)

            if selected_zombie:
                messagebox.showinfo("NOTE",f"You use {self.selected_weapon_name} attacked {selected_zombie.name}")
                self.mylog(f'You use {self.selected_weapon_name} attacked {selected_zombie.name}')
                zombie_window.destroy()
                for item in self.game.store.product:
                    if self.selected_weapon_name == item.name:
                        weapon = item
                self.game.attackZombie(selected_zombie,weapon)
                self.update_coin_label()
                self.refresh()
                if self.game.player.health <= 0:
                    self.mylog('You lose the game')
                    messagebox.showinfo("GAME OVER", "SORRY! YOU KILLED BY ZOMBIES!")
                    self.frame1.destroy()
                    self.frame2.destroy()
                    myApp = My_thirdUI(self.root)



    def refresh(self):
        """
        refresh the room condition after doing command
        :return:
        """
        if self.game.currentRoom.getName() =="firststreet":
            self.first_street()
        elif self.game.currentRoom.getName() == "policestation":
            self.policestation()
        elif self.game.currentRoom.getName() == "saferoom":
            self.saferoom()
        elif self.game.currentRoom.getName() == "supermarket":
            self.supermarket()
        elif self.game.currentRoom.getName() == "secondStreet":
            self.second_street()
        elif self.game.currentRoom.getName() =="campus":
            self.campus()
        elif self.game.currentRoom.getName() == "firstfloor":
            self.firstfloor()
        elif self.game.currentRoom.getName() == "basement":
            self.basement()
        elif self.game.currentRoom.getName() == "secondfloor":
            self.secondfloor()
        else:
            self.rooftop()


    def get_zombie_object(self, zombie_name):
        '''got zombie from zombie_name'''
        zombies = self.game.currentRoom.getZombies()

        for zombie in zombies:
            if zombie.name == zombie_name:
                return zombie

        # if can't find it
        return None

    def get_weapon_object(self, weapon_name):
        '''Get the weapon object based on its name'''
        for item in self.game.player.inventory:
            if item.name == weapon_name:
                return item
        return None

    def load_items_in_room(self, zombies_x, zombies_y):
        """
        Load the items in the room when zombies are defeated
        :param zombies_x:
        :param zombies_y:
        :return:
        """
        try:
            self.item_images = {}
            items = self.game.currentRoom.items
            zombies_y += 30
            for item in items:
                # print(item.name)
                item_path = self.get_items_image_path(item.name)
                # print(item_path)
                item_img = Image.open(item_path)
                item_img = item_img.resize((30, 30), Image.LANCZOS)

                item_image = ImageTk.PhotoImage(item_img)
                self.item_images[item.name] = item_image
                self.current_scene_canvas.create_image(zombies_x, zombies_y, anchor=NW, image=item_image)
                zombies_x += 60
        except Exception as e:
            # Handle the exception here, you might want to log the error or show a message to the user
            print(f"An error occurred: {e}")

    def load_zombie(self, zombies_x, zombies_y):
        """
        add zombies into room
        :param zombies_x:
        :param zombies_y:
        :return:
        """
        if self.game.currentRoom.haszombies():
            zombies = self.game.currentRoom.getZombies()
            for zombie in zombies:
                #print(zombie.name)
                zombie_path = self.get_zombies_image_path(zombie.name)
                #print(zombie_path)
                zombie_img = Image.open(zombie_path)
                zombie_img = zombie_img.resize((50, 80), Image.LANCZOS)

                # Create a unique ImageTk.PhotoImage for each zombie
                zombie_image = ImageTk.PhotoImage(zombie_img)

                # Store the zombie images in a dictionary with zombie name as key
                self.zombie_images[zombie.name] = zombie_image

                # Create a new image on canvas for each zombie
                self.current_scene_canvas.create_image(zombies_x, zombies_y, anchor=NW, image=zombie_image)

                zombies_x += 60


    def get_zombies_image_path(self,zombie_name):
        """
        load the image of zombies
        :param zombie_name:
        :return:
        """
        image_mapping = {
            "weak-zombie":"images/zombies/weak-zombie.png",
            "little-zombie":"images/zombies/little-zombie.jpg",
            "normal-zombie":"images/zombies/normal-zombie.png",
            "strong-zombie":"images/zombies/strong-zombie.png",
            "walk_zombie":"images/zombies/walk-zombie.png",
            "crazy-zombie":"images/zombies/crazy-zombie.png",
            "huge-zombie":"images/zombies/huge-zombie.png",
            "small-zombie":"images/zombies/small-zombie.png",
            "quite-zombie":"images/zombies/quite-zombie.png",
            "cute-zombie":"images/zombies/cute-zombie.png",
            "calm-zombie":"images/zombies/calm-zombie.png",
            "default": "images/gun.png"

        }
        return image_mapping.get(zombie_name, "images/gun.png")

    # Assuming you have a function to get the image path based on weapon_name
    def get_items_image_path(self,weapon_name):
        # Implement this function to return the image path based on the weapon_name
        # For example, you might have a mapping of weapon names to image paths
        # Replace this with your actual implementation
        image_mapping = {
            "Little-knife": "images/little_knife.jpg",
            "Big-knife": "images/big_knife.png",
            "sword":"images/sward.png",
            "Gun":"images/gun.png",
            "little-cure":"images/little_cure.png",
            "first_aid_kit":"images/first_aid_kit.png",
            "final-key":"images/key.png",
            # Add more mappings as needed
            "default": "images/gun.png"
        }
        return image_mapping.get(weapon_name,"images/gun.png")  # Replace default with an actual default image path



    def choose_cure(self):
        '''Check weapon'''
        medicine = [item for item in self.game.player.inventory if item.type == "medicine"]
        # Create a dictionary to store weapon names as keys and their quantities as values
        cure_counts = {}

        # Count the quantities of each weapon
        for cure in medicine:
            cure_name = cure.name
            cure_quantity = 1

            # If the cure name is not in the dictionary, add it with the quantity as the value
            if cure_name not in cure_counts:
                cure_counts[cure_name] = cure_quantity
            else:
                # If the cure name is already in the dictionary, increment the quantity
                cure_counts[cure_name] += cure_quantity

        # Create a new window for displaying weapons
        cure_window = tk.Toplevel(self.root)
        cure_window.title("Choose medicine")
        cure_window.geometry("400x400")

        # Create a frame to hold weapon information
        cure_frame = ttk.Frame(cure_window)
        cure_frame.grid(row=0, column=0, padx=10, pady=10)

        # Iterate through weapon_counts and display information
        for cure_name, quantity in cure_counts.items():
            label_text = f"{cure_name} - Quantity: {quantity}"

            # Assuming you have a function to get the image path based on weapon_name
            image_path = self.get_items_image_path(cure_name)

            # Load and resize the weapon image
            cure_image = Image.open(image_path)
            cure_image = cure_image.resize((50, 50), Image.LANCZOS)  # Adjust size as needed
            cure_image = ImageTk.PhotoImage(cure_image)

            # Create a button with the weapon information and image
            cure_button = ttk.Button(cure_frame, text=label_text, image=cure_image, compound=tk.LEFT,
                                       command=lambda name=cure_name: self.recover(cure_name,cure_window))

            cure_button.image = cure_image  # Keep a reference to prevent image from being garbage collected
            cure_button.pack(pady=5)

    def choose_item_from_room(self):
        """
        choose the item you want to pick
        :return:
        """
        room_items = self.game.currentRoom.items
        # Create a new window for displaying backpack items
        backpack_window = tk.Toplevel()
        backpack_window.title("Choose Item to Pick Up")
        backpack_window.geometry("400x400")


        # Create a frame to hold item information
        item_frame = ttk.Frame(backpack_window)
        item_frame.grid(row=0, column=0, padx=10, pady=10)

        # Iterate through backpack items and display information
        for item in room_items:
            label_text = f"{item.name}"

            # Assuming you have a function to get the image path based on item name
            image_path = self.get_items_image_path(item.name)

            # Load and resize the weapon image
            item_image = Image.open(image_path)
            item_image = item_image.resize((50, 50), Image.LANCZOS)  # Adjust size as needed
            item_image = ImageTk.PhotoImage(item_image)

            # Create a button with the item information and image
            item_button = ttk.Button(item_frame, text=label_text, image=item_image, compound=tk.LEFT,
                                     command=lambda chosen_item=item: self.pickItem(chosen_item,backpack_window))
            item_button.image = item_image  # Keep a reference to prevent image from being garbage collected
            item_button.pack(pady=5)

    def pickItem(self, item,backpack_window):
        """
        pick the items from room
        :param item:
        :param backpack_window:
        :return:
        """
        after_size = self.game.player.max_inventory_size - item.weight
        if after_size<0:
            messagebox.showinfo("NOTE","Sorry, your backpack is full, drop something before you pick.")
        else:
            backpack_window.destroy()
            # Handle the logic for picking up the selected item
            self.game.doTakeCommand(item.name)
            #print(f"Picked up {item.name}")
            self.mylog(f'Picked up {item.name}')
            self.refresh()
            self.update_coin_label()


    def recover(self,cure_name,cure_window):
        """
        can use medicine to recover
        :param cure_name:
        :param cure_window:
        :return:
        """
        for item in self.game.player.inventory:
            if item.name == cure_name:
                self.game.docureCommand(item)
                break

        self.update_coin_label()
        cure_window.destroy()
        self.refresh()

    def buy_stuff(self):
        """
        choose the item you want to buy
        :return:
        """
        stuffs = self.game.store.product
        store_window = tk.Toplevel()
        store_window.title("Store")
        store_window.geometry("600x400")

        # Create a frame to hold item information
        store_frame = ttk.Frame(store_window)
        store_frame.grid(row=0, column=0, padx=10, pady=10)

        # Define the number of columns
        num_columns = 2

        # Iterate through backpack items and display information
        for idx, item in enumerate(stuffs):
            label_text = f"Name: {item.name} ( Price: {item.price})"

            # Assuming you have a function to get the image path based on item name
            image_path = self.get_items_image_path(item.name)

            # Load and resize the item image
            item_image = Image.open(image_path)
            item_image = item_image.resize((50, 50), Image.LANCZOS)  # Adjust size as needed
            item_image = ImageTk.PhotoImage(item_image)

            # Calculate row and column indices
            row_index = idx // num_columns
            col_index = idx % num_columns

            # Create a button with the item information and image
            item_button = ttk.Button(store_frame, text=label_text, image=item_image, compound=tk.LEFT,
                                     command=lambda buy_stuff=item: self.buy_item(buy_stuff, store_window))
            item_button.image = item_image  # Keep a reference to prevent image from being garbage collected
            item_button.grid(row=row_index, column=col_index, padx=5, pady=5)


    def buy_item(self,stuff,store_window):
        """
        buy item
        :param stuff:
        :param store_window:
        :return:
        """
        self.game.store.buyProduct(self.game.player,stuff)
        self.mylog(f'bought {stuff.name}')
        store_window.destroy()
        self.update_coin_label()
        self.refresh()

    def Up(self):
        """
        go upstairs
        :return:
        """
        self.mylog('go up')
        self.gocommand("upstairs")
        self.close_previous_scene()
        if self.game.currentRoom.haszombies():
            self.game.do_attack_player()
            if self.game.player.health<=0:
                self.mylog('You lose the game')
                messagebox.showinfo("GAME OVER", "SORRY! YOU KILLED BY ZOMBIES!")
                self.frame1.destroy()
                self.frame2.destroy()
                myApp = My_thirdUI(self.root)
            self.update_coin_label()
            self.refresh()

    def Down(self):
        """
        go down stairs
        :return:
        """
        self.mylog('go down')
        self.gocommand("downstairs")
        self.close_previous_scene()
        if self.game.currentRoom.haszombies():
            self.game.do_attack_player()
            if self.game.player.health<=0:
                self.mylog('You lose the game')
                messagebox.showinfo("GAME OVER", "SORRY! YOU KILLED BY ZOMBIES!")
                self.frame1.destroy()
                self.frame2.destroy()
                myApp = My_thirdUI(self.root)
            self.update_coin_label()
            self.refresh()

    def North(self):
        """
        the direction of go north
        :return:
        """
        self.mylog('go north')
        self.gocommand("north")
        self.close_previous_scene()
        if self.game.currentRoom.haszombies():
            self.game.do_attack_player()
            if self.game.player.health<=0:
                self.mylog('You lose the game')
                messagebox.showinfo("GAME OVER", "SORRY! YOU KILLED BY ZOMBIES!")
                self.frame1.destroy()
                self.frame2.destroy()
                myApp = My_thirdUI(self.root)
            self.update_coin_label()
            self.refresh()


    def South(self):
        """
        the direction of go south
        :return:
        """
        self.mylog('go south')
        self.gocommand("south")
        self.close_previous_scene()
        if self.game.currentRoom.haszombies():
            self.game.do_attack_player()
            if self.game.player.health<=0:
                self.mylog('You lose the game')
                messagebox.showinfo("GAME OVER", "SORRY! YOU KILLED BY ZOMBIES!")
                self.frame1.destroy()
                self.frame2.destroy()
                myApp = My_thirdUI(self.root)
            self.update_coin_label()
            self.refresh()

    def East(self):
        """
        the direction of  esat
        :return:
        """
        self.mylog('go east')
        self.gocommand("east")
        self.close_previous_scene()
        if self.game.currentRoom.haszombies():
            self.game.do_attack_player()
            if self.game.player.health<=0:
                self.mylog('You lose the game')
                messagebox.showinfo("GAME OVER", "SORRY! YOU KILLED BY ZOMBIES!")
                self.frame1.destroy()
                self.frame2.destroy()
                myApp = My_thirdUI(self.root)
            self.update_coin_label()
            self.refresh()

    def West(self):
        """
        the direction of west
        :return:
        """
        self.mylog('go west')
        self.gocommand("west")
        self.close_previous_scene()
        if self.game.currentRoom.haszombies():
            self.game.do_attack_player()
            if self.game.player.health<=0:
                self.mylog('You lose the game')
                messagebox.showinfo("GAME OVER", "SORRY! YOU KILLED BY ZOMBIES!")
                self.frame1.destroy()
                self.frame2.destroy()
                myApp = My_thirdUI(self.root)
            self.update_coin_label()
            self.refresh()


    def gocommand(self,word):
        """
        it can help for go next room
        :param word:
        :return:
        """
        nextRoom = self.game.currentRoom.getExit(word)
        self.game.currentRoom =nextRoom
        if self.game.currentRoom.getName() =="firststreet":
            self.first_street()
        elif self.game.currentRoom.getName() == "policestation":
            self.policestation()
        elif self.game.currentRoom.getName() == "saferoom":
            self.saferoom()
        elif self.game.currentRoom.getName() == "supermarket":
            self.supermarket()
        elif self.game.currentRoom.getName() == "secondStreet":
            self.second_street()
        elif self.game.currentRoom.getName() =="campus":
            self.campus()
        elif self.game.currentRoom.getName() == "firstfloor":
            self.firstfloor()
        elif self.game.currentRoom.getName() == "basement":
            self.basement()
        elif self.game.currentRoom.getName() == "secondfloor":
            self.secondfloor()
        else:
            self.rooftop()




    def help(self, *args):
        '''background introduction'''
        command = self.v.get()
        self.mylog('Help-background introduction')
        if command == 'background introduction':
            messagebox.showinfo("Background", "A virus has leaked from the city's labs and infected zombies roam the streets. "
                                              "\nYour daughter has gotten separated and is trapped in the school basement."
                                              "\nWhat you need to do?"
                                              "\nAt first time, you are in the safe room. And this room has no zombies."
                                              "\nWhen you getting into a new area, you need to defeated all the zombies in the area."
                                              "\nYou can take the weapon from space without zombies."
                                              "\nThen you can go to next room."
                                              "\nYou need to save your daughter and bring her to the rooftop of the school building. "
                                              "\nThere will have helicopter to save you to a safe city!!!"
                                              )

        #button introduction
        elif command == 'button introduction':
            messagebox.showinfo("Button", "HELP:Function Introduction"
                                          "\nQUIT: Exit the game"
                                          "\nBAG: You can check and drop items here"
                                          "\nDIRECTION: Check exits"
                                          "\nWEAPON: Check how many weapons you own"
                                          "\nKEY: Check if you have final-key"
                                          "\nMONEY: Check how many money you own"
                                          "\nLIFE: Check your health value"
                                          "\nATTACK: Use weapon to attack zombies"
                                          "\nCURE: Check your keys number"
                                          "\nPICK: Can pick the supplies in the room"
                                          "\nSTORE: Using money to buy supplies in store")
        elif command == 'keyboard control':
            messagebox.showinfo("keyboard control","'A' can control player go left"
                                         "\n'D' can control player go right")


    def about(self):
        '''
            View game background
        '''
        self.mylog('View game background')
        messagebox.showinfo("Background", "The whole city has fallen."
                                          "\nSave your daughter and escape the city."
                                          "\nCome on! Warrior! ")

    def cure_command(self):
        """
        cure function
        :return:
        """
        self.mylog('use cure command')
        self.choose_cure()



    def attack_command(self):
        """
        attack function
        :return:
        """
        self.mylog('attack zombies')
        self.choose_weapon()

    def store_command(self):
        """
        it's for store command
        :return:
        """
        self.mylog('using store')
        self.buy_stuff()



    def pick_command(self):
        """
        it's a function of pick command button
        :return:
        """
        self.mylog('using pick command')
        self.choose_item_from_room()

    def mylog(self, action):
        """
           Create a log to record the user's action
        """
        with open("log.txt", "a") as f:
            f.write("\n------------------------------------------------------------------------------\n")
            f.write(str(datetime.datetime.now()) + '\n')
            f.write(str(action + '\n'))
            f.close()




class My_thirdUI:
    """
    By using third UI, we can get the endgame UI from it
    """
    def __init__(self, root):
        # Create the model instance ...
        self.root = root
        self.game_again = Game()
        self.root.config()
        self.overframe = tk.Frame(self.root, width=1100, height=600)
        self.overframe.pack_propagate(0)  # Prevents resizing
        self.overframe.pack(side=TOP)
        self.gameover_image = ImageTk.PhotoImage(Image.open('images/gameover.png'))
        self.gameover = tk.Label(self.overframe, image=self.gameover_image, width=1100, height=468)
        self.gameover.pack(side=TOP)
        self.button_again = tk.Button(self.overframe, text="PLAY AGAIN", command=lambda: self.change(),
                                      font=('Sans', '12', 'bold'))
        self.button_again.place(x=400, y=450)

        self.button_down = tk.Button(self.overframe, text="END GAME", command=lambda: self.end(),
                                     font=('Sans', '12', 'bold'))
        self.button_down.place(x=600, y=450)

    def change(self):
        """
            close the  secondUI and start the firstUI
        """
        self.overframe.destroy()
        myApp = My_firstUI(self.root, 0)

    def end(self):
        self.root.destroy()

def main():
    win = tk.Tk()  # Create a window
    win.title("KILL ZOMBIES")  # Set window title
    win.geometry("1100x650")  # Set window size
    win.resizable(False, False)  # Both x and y dimensions ...
    # Create the GUI as a Frame
    # and attach it to the window ...
    myApp = My_firstUI(win, 0)
    # Call the GUI mainloop ...
    win.mainloop()


if __name__ == "__main__":
    main()