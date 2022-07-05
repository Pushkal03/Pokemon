from tkinter import *
import random
from PIL import ImageTk, Image

root=Tk()
root.title("Endless Pokemon Game")
root.geometry("800x500")
root.configure(background="orangered1")

bulbasour = ImageTk.PhotoImage(Image.open ("bulbasour.jpg"))
pikachu = ImageTk.PhotoImage(Image.open ("pikachu.jpg"))
abra = ImageTk.PhotoImage(Image.open ("abra.jpg"))
ratata = ImageTk.PhotoImage(Image.open ("ratata.jpg"))
persion = ImageTk.PhotoImage(Image.open ("persion.jpg"))
squirtle = ImageTk.PhotoImage(Image.open ("squirtle.jpg"))
nidoking = ImageTk.PhotoImage(Image.open ("nidoking.jpg"))
meowth = ImageTk.PhotoImage(Image.open ("meowth.jpg"))
kadabra = ImageTk.PhotoImage(Image.open ("kadabra.jpg"))
jigglypuff = ImageTk.PhotoImage(Image.open ("jigglypuff.jpg"))
charmender = ImageTk.PhotoImage(Image.open ("charmender.jpg"))
button = ImageTk.PhotoImage(Image.open ("button.jpg"))

pokemon_images = [bulbasour,pikachu,abra,ratata,persion,squirtle,nidoking,meowth,kadabra,jigglypuff,charmender]
pokemon_score = [60,200,30,40,70,50,90,60,70,70,50]

player_score1 = 0

def player1():
    global player_score1
    rand1 = random.randint(0,10)
    random_pokemon = pokemon_images[rand1]
    random_pokemon3["image"] = random_pokemon
    random_power_list = pokemon_score[rand1]
    player_score1 = player_score1 + random_power_list
    player1_score["text"] = player_score1
        
player_score2 = 0

def player2():
    global player_score2
    rand2 = random.randint(0,10)
    random_pokemon1 = pokemon_images[rand2]
    random_pokemon3["image"] = random_pokemon1
    random_power_list1 = pokemon_score[rand2]
    player_score2 = player_score2 + random_power_list1
    player2_score["text"] = player_score2
    
btn1 = Button(root,image=button,command=player1)
btn1.place(relx=0.1,rely=0.7,anchor=CENTER)

btn2 = Button(root,image=button,command=player2)
btn2.place(relx=0.9,rely=0.7,anchor=CENTER)


player1 = Label(root, text="Player 1", bg="greenyellow",fg="black")
player1.place(relx=0.1,rely=0.3,anchor=CENTER)

player2 = Label(root, text="Player 2", bg="greenyellow",fg="black")
player2.place(relx=0.9,rely=0.3,anchor=CENTER)

player1_score = Label(root, text="", bg="lightslateblue",fg="white")
player1_score.place(relx=0.1,rely=0.4,anchor=CENTER)

player2_score = Label(root, text="", bg="lightslateblue",fg="white")
player2_score.place(relx=0.9,rely=0.4,anchor=CENTER)

random_pokemon3 = Label(root, bg="white",fg="black")
random_pokemon3.place(relx=0.5,rely=0.5,anchor=CENTER)

root.mainloop()