
from tkinter import ttk
from tkinter import * 
from PIL  import ImageTk, Image
import random


root = Tk()
root.geometry("740x481+300+100")
root.resizable(False, False)
root.title("hajara waraka mikass")
root.iconbitmap('paper.ico')


#variabels
list = ["hajara", "mikass", "waraka"]
x1 = 0
x2 = 0

#======= def =====

#start
def gamestart():
    a5tar.place(x=40, y=40)
def letsgo():
    game.place(x=40, y=40)

# game loop

def go():
    global x1 
    global x2
    
    for i in range(3):
        car1 = random.choice(list)
        if car1 == "hajara":
            hajara1 = Label(hand1, image=ph1)
            hajara1.place(x=0, y=0)
        elif car1 == "mikass":
            mikass1 = Label(hand1, image=pm1)
            mikass1.place(x=0, y=0)
        elif car1 == "waraka":
            waraka1 = Label(hand1, image=pw1)
            waraka1.place(x=0, y=0)

        car2 = random.choice(list)
        if car2 == "hajara":
            hajara2 = Label(hand2, image=ph2)
            hajara2.place(x=0, y=0)
        elif car2 == "mikass":
            mikass2 = Label(hand2, image=pm2)
            mikass2.place(x=0, y=0)
        elif car2 == "waraka":
            waraka2 = Label(hand2, image=pw2)
            waraka2.place(x=0, y=0)

    # score of players
    
    if car1 == "hajara" and car2 == "waraka":
        s1 = x1 + 1
        x1 = s1
        sp1 = Label(game, text=s1, font=("Fixedsys", 20), width=5, height=1)
        sp1.place(x=70, y=80)
    if car2 == "hajara" and car1 == "waraka":
        s2 = x2 + 1
        x2 = s2
        sp2 = Label(game, text=s2, font=("Fixedsys", 20), width=5, height=1)
        sp2.place(x=490, y=80)
    
    if car1 == "waraka" and car2 == "mikass":
        s1 = x1 + 1
        x1 = s1
        sp1 = Label(game, text=s1, font=("Fixedsys", 20), width=5, height=1)
        sp1.place(x=70, y=80)
    if car2 == "waraka" and car1 == "mikass":
        s2 = x2 + 1
        x2 = s2
        sp2 = Label(game, text=s2, font=("Fixedsys", 20), width=5, height=1)
        sp2.place(x=490, y=80)

    if car1 == "mikass" and car2 == "hajara":
        s1 = x1 + 1
        x1 = s1
        sp1 = Label(game, text=s1, font=("Fixedsys", 20), width=5, height=1)
        sp1.place(x=70, y=80)
    if car2 == "mikass" and car1 == "hajara":
        s2 = x2 + 1
        x2 = s2
        sp2 = Label(game, text=s2, font=("Fixedsys", 20), width=5, height=1)
        sp2.place(x=490, y=80)

    # winer

    if str(x1) == tor7.get():
        win1 = Frame(root, width=660, height=400, bg="white")
        win1.place(x=40, y=40)
        winer1 = Label(win1 ,text="Player 1 is Winer", font=("Fixedsys", 35))
        winer1.place(x=50, y=50)

    if str(x2) == tor7.get():
        win2 = Frame(root, width=660, height=400, bg="white")
        win2.place(x=40, y=40)
        winer2 = Label(win2 ,text="Player 2 is Winer", font=("Fixedsys", 35))
        winer2.place(x=50, y=50)
 




#======== Background ========
imgbg = ImageTk.PhotoImage(Image.open('background.png'))
my_canves = Canvas(root, width=740, height=481)
my_canves.pack(fill="both", expand=True)
my_canves.create_image(0, 0, image=imgbg, anchor="nw")

#======= Lobby =======
my_canves.create_text(370, 160, text="Welcom!", font=("Fixedsys", 50, "bold"), fill="#5249b6")
my_canves.create_text(630, 460, text="By me : Khalil Andolsi", font=("Segoe Print", 13), fill="black")
start = Button(root, text="Start", command=gamestart, font=("Fixedsys", 20, "bold"), fg="black", bg="#817aca", activebackground="#5148b5", bd=3)
start.place(x=300, y=220)


#a5tar 
a5tar = Frame(root, width=660, height=400, bg="white")
qu = Label(a5tar, text="3la 9adech bech tal3ib??", font=("Fixedsys", 20, "bold"))
qu.place(x=130, y=130)
tor7 = StringVar()
ch = ttk.Combobox(a5tar, textvariable=tor7, state='readonly', font=("Fixedsys", 20, "bold"), width=5)
ch['values'] = ("3", "5", "10", "15", "20", "25", "40", "50", "75", "90", "100")
ch.place(x=280, y=200)
startg = Button(a5tar, text="Let's Goooooo", bd=5, font=("Fixedsys", 20, "bold"), bg="black", fg="white", command=letsgo)
startg.place(x=200, y=280)




#======= Game ========= 
game = Frame(root, width=660, height=400, bg="white")

#players
player1 = Label(game, text="player1", font=("Fixedsys", 17))
player1.place(x=60, y=30)

player2 = Label(game, text="player2", font=("Fixedsys", 17))
player2.place(x=480, y=30)

vs = Label(game, text="VS", font=("Fixedsys", 17))
vs.place(x=300, y=80)

#score
sp1 = Label(game, text=0, font=("Fixedsys", 20), width=5, height=1)
sp1.place(x=70, y=80)

sp2 = Label(game, text=0, font=("Fixedsys", 20), width=5, height=1)
sp2.place(x=490, y=80)

#go button
gow = Button(game, text="Go", font=("Fixedsys", 17), bg="black", fg="white", width=6, height=1, command=go)
gow.place(x=275, y=225)

#hands frame
hand1 = Frame(game, width=260, height=180, bg="white")
hand1.place(x=0, y=170)

hand2 = Frame(game, width=260, height=180, bg="white")
hand2.place(x=400, y=170)


#======= Photos ==========

#hajara
phajara1 = Image.open('player1/hajara1.png')
resized = phajara1.resize((260, 180), Image.ANTIALIAS)
ph1 = ImageTk.PhotoImage(resized)
hajara1 = Label(hand1, image=ph1)
hajara1.place(x=0, y=0)

phajara2 = Image.open('player2/hajara2.png')
resized = phajara2.resize((260, 180), Image.ANTIALIAS)
ph2 = ImageTk.PhotoImage(resized)
hajara2 = Label(hand2, image=ph2)
hajara2.place(x=0, y=0)

#mikass
pmikass1 = Image.open('player1/mikass1.png')
resized = pmikass1.resize((260, 180), Image.ANTIALIAS)
pm1 = ImageTk.PhotoImage(resized)
mikass1 = Label(hand1, image=pm1)

pmikass2 = Image.open('player2/mikass2.png')
resized = pmikass2.resize((260, 180), Image.ANTIALIAS)
pm2 = ImageTk.PhotoImage(resized)
mikass2 = Label(hand2, image=pm2)

#waraka
pwaraka1 = Image.open('player1/waraka1.png')
resized = pwaraka1.resize((260, 180), Image.ANTIALIAS)
pw1 = ImageTk.PhotoImage(resized)
waraka1 = Label(hand1, image=pw1)

pwaraka2 = Image.open('player2/waraka2.png')
resized = pwaraka2.resize((260, 180), Image.ANTIALIAS)
pw2 = ImageTk.PhotoImage(resized)
waraka2 = Label(hand2, image=pw2)




root.mainloop()