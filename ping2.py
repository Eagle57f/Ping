import os, tkinter
from time import strftime, sleep
from datetime import datetime
from threading import *

exit=False

def ftkinter():
    global gui
    gui = tkinter.Tk()
    btn = tkinter.Button(gui, text ="Exit", command = fexit)
    btn.pack()
    Thread(target=prg).start()
    gui.mainloop()

def fexit():
    global exit
    exit=True
    gui.destroy()
    return exit

def prg():
    var=True
    with open(f"{os.path.dirname(__file__)}\\ping.txt", "a") as fichier:
        heuredebuttest = datetime.now()
        dureecoupures = 0
        nombrecoupures = 0
        while exit == False:
            sleep(0.1)
            response = os.system("ping -n 1 google.com")
            a = datetime.now()
            heure = strftime(a.strftime("%Y-%m-%d %H:%M:%S"))

            if response == 1 and var == True:
                heuredebut=a
                fichier.write(f"Début de coupure: {heure}\t")
                var=False

            if response == 0 and var == False:
                heurefin=datetime.now()

                if dureecoupures == 0:
                    dureecoupures = heurefin - heuredebut
                else:
                    dureecoupures = dureecoupures + (heurefin - heuredebut)
                fichier.write(f"Fin de coupure: {heure}\tDurée de coupure: {str(heurefin - heuredebut)}\n")
                nombrecoupures += 1
                fichier.close()
                fichier = open(f"{os.path.dirname(__file__)}\\ping.txt", "a")
                var=True
        dureetest = datetime.now() - heuredebuttest
        if nombrecoupures != 0:
            moyennecoupures = dureecoupures/nombrecoupures
        else:
            moyennecoupures = "0"
        fichier.write(f"""
    ---------------------------------------------------------------
    Début du test: {heuredebuttest}
    Fin du test: {datetime.now()}
    Durée du test: {dureetest}

    Nombre de coupures: {nombrecoupures}
    Durée totale des coupures: {dureecoupures}
    Durée moyenne des coupures: {moyennecoupures}
    ---------------------------------------------------------------

""")



ftkinter()
