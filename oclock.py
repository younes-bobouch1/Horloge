from tkinter import *
from time import strftime
#from tkinter import messagebox
from tkinter import simpledialog

#très compliqué de créer les fonctions pour changer l'heure, mettre une alarme etc...
#aucune ressource trouver sur internet

#créer ma fenêtre
gui = Tk()
"------------------------------------------------------------------------------------------------------------------"
#titre
gui.title("Clock")
"------------------------------------------------------------------------------------------------------------------"
#taille de la fenêtre
gui.geometry("390x300")

def heures():
    string=strftime("%H:%M:%S %p")
    clock.config(text=string)
    clock.after(1000,heures)

def halarme():
    string=strftime("%H:%M:%S %p")
    lalarme.config(text=string)
    lalarme.after(1000,halarme)

def change_heures():
    simpledialog.askstring("Réglage de l'heure", "Format = HH : MM : SS", parent=gui)

def alarme():
    simpledialog.askstring("Alarme", "Format de l'alarme = HH : MM : SS", parent=gui)

txt_heure = Label(gui,text="Heure : ",font=("arial",15,"bold"),fg="black")
txt_heure.place(x=150, y=10)

clock = Label(gui,font=("Courier",25,"bold"),fg="black")
clock.place(x=80, y=40)

lalarme = Label(gui,font=("Courier",25,"bold"),fg="grey")
lalarme.place(x=80, y=150)

boutton_changer_heure = Button(gui,text="CHANGER L'HEURE",fg="black",font=("arial",10),bg="grey",command=change_heures)
boutton_changer_heure.place(x=110, y=200,height=40,width=160)

boutton_alarme = Button(gui,text="ALARME",fg="black",font=("arial",10),bg="grey",command=alarme)
boutton_alarme.place(x=110, y=250,height=40,width=160)

txt_alarme = Label(gui,text="Alarme à : ",font=("arial",15,"bold"),fg="grey")
txt_alarme.place(x=140, y=110)


heures()
halarme()
gui.mainloop()