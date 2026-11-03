import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from pyo import *
import threading
from effets import Effets
import time
from PyQt5.QtCore import QObject
import sys
import json 

import tkinter as tk


class Ajust3():
 




   def __init__(self):
        # Ces objets deviennent des attributs de cette instance
        self.server = Server( nchnls=1,sr=44100,buffersize=1024, duplex=1)
        self.server.setOutputDevice(2)  
        self.server.boot()
        #s.start()
        self.server.start()
        self.mic = Input()
        self.mic.out()  # Renvoie le son du micro vers la sortie audio

        self.server.recordOptions(
         filename="son.wav",
         fileformat=0,  # WAV
         sampletype=0   # 16 bits
         )





   
   #s = Server( nchnls=1,sr=44100,buffersize=1024, duplex=1)
   """
   #s.setInputDevice(0)   # À remplacer par l'identifiant de votre entrée
   s.setOutputDevice(2) 
   #s.setOutputDevice(2)   
#
   s.boot()
   s.start()
   
   mic = Input() 
   """   



  # Crée la fenêtre
  #fenetre = tk.Tk()
  #fenetre.title("Exemple de slider")
  

  # Fonction appelée quand la valeur change
   def afficher_valeur(valeur):
      Ajust3.etiquette.config(text=f"Valeur sélectionnée : {valeur}")
      with open("effets.json", "r", encoding="utf-8") as fichier:
        donnees = json.load(fichier)
      if (int(valeur)<= 7 & int(valeur)>= -7):
       donnees["tanspoHarmonizer"] = int(valeur)
      else : donnees["tanspoHarmonizer"] = 0

      
      with open("effets.json", "w", encoding="utf-8") as fichier:
        json.dump(donnees, fichier, ensure_ascii=False, indent=2)
       
        ef = Effets()

        reverbe = ef.Harmonizer()


      

   """
   def afficher_valeur2(valeur):
      Ajust.etiquette2.config(text=f"Valeur sélectionnée : {valeur}")
      with open("effets.json", "r", encoding="utf-8") as fichier:
        donnees = json.load(fichier)
      if (float(valeur) <= 1):
        donnees["dampReverb"] = float(valeur)
      else : donnees["dampReverb"] = 1

      with open("effets.json", "w", encoding="utf-8") as fichier:
        json.dump(donnees, fichier, ensure_ascii=False, indent=2)

        ef = Effets()

        reverbe = ef.Reverb()



   def afficher_valeur3(valeur):
      Ajust.etiquette3.config(text=f"Valeur sélectionnée : {valeur}")
      with open("effets.json", "r", encoding="utf-8") as fichier:
        donnees = json.load(fichier)
      if (float(valeur) <= 1):
        donnees["balReverb"] = float(valeur)
      else : donnees["balReverb"] = 1

      
      with open("effets.json", "w", encoding="utf-8") as fichier:
        json.dump(donnees, fichier, ensure_ascii=False, indent=2)

        ef = Effets()

        reverbe = ef.Reverb()



   """

 # Fonction appelée quand la valeur change
   def afficher_valeur4(valeur):
      Ajust3.etiquette4.config(text=f"Valeur sélectionnée : {valeur}")
      with open("effets.json", "r", encoding="utf-8") as fichier:
        donnees = json.load(fichier)
      if (int(valeur) <= 1000 & int(valeur)>= 0 ):
        donnees["freqLowpass"] = int(valeur)
      else : donnees["freqLowpass"] = 1000

      
      with open("effets.json", "w", encoding="utf-8") as fichier:
        json.dump(donnees, fichier, ensure_ascii=False, indent=2)

        ef = Effets()

        chorus = ef.Lowpass()


# Fonction appelée quand la valeur change
   def afficher_valeur5(valeur):
      Ajust3.etiquette4.config(text=f"Valeur sélectionnée : {valeur}")
      with open("effets.json", "r", encoding="utf-8") as fichier:
        donnees = json.load(fichier)
      if (int(valeur) <= 4 & int(valeur) >= 1):
        donnees["orderLowpass"] = float(valeur)
      else : donnees["orderLowpass"] = 1

      
      with open("effets.json", "w", encoding="utf-8") as fichier:
        json.dump(donnees, fichier, ensure_ascii=False, indent=2)

        ef = Effets()

        chorus = ef.Lowpass()


   """

# Fonction appelée quand la valeur change
   def afficher_valeur6(valeur):
      Ajust.etiquette4.config(text=f"Valeur sélectionnée : {valeur}")
      with open("effets.json", "r", encoding="utf-8") as fichier:
        donnees = json.load(fichier)
      if (float(valeur) <= 1):
        donnees["balChorus"] = float(valeur)
      else : donnees["balChorus"] = 1

      
      with open("effets.json", "w", encoding="utf-8") as fichier:
        json.dump(donnees, fichier, ensure_ascii=False, indent=2)

        ef = Effets()

        chorus = ef.Chorus()


    """









   def Harmonizer():

      
      fenetre = tk.Tk()
      

      fenetre.title("Reglage Harmonizer")

      # Crée un slider de 1 à 3
      slider = tk.Scale(
         fenetre,
         from_= -7,                 # Valeur minimale
         to=7,
         resolution=1,                  # Valeur maximale
         orient="horizontal",     # Curseur horizontal
         label="Tune or detune",
         command=Ajust3.afficher_valeur
         )
      slider.pack(padx=20, pady=10)

      # Affiche la valeur actuelle
      Ajust3.etiquette = tk.Label(fenetre, text=f"Valeur sélectionnée : {slider.get()}")
      Ajust3.etiquette.pack(pady=10)



      """
       # Crée un slider de 0.01 à 1
      slider2 = tk.Scale(
         fenetre,
         from_=0.01,                 # Valeur minimale
         to=1,                 
         resolution=0.02,                  # Valeur maximale
         orient="horizontal",     # Curseur horizontal
         label="Damp",
         command=Ajust.afficher_valeur2
         )
      slider2.pack(padx=20, pady=10)

      # Affiche la valeur actuelle
      Ajust.etiquette2 = tk.Label(fenetre, text=f"Valeur sélectionnée : {slider2.get()}")
      Ajust.etiquette2.pack(pady=10)

       # Crée un slider de 0 à 1
      slider3 = tk.Scale(
         fenetre,
         from_=0,                 # Valeur minimale
         to=1,
         resolution=0.1,                  # Valeur maximale
         orient="horizontal",     # Curseur horizontal
         label="Balance",
         command=Ajust.afficher_valeur3
         )
      slider3.pack(padx=20, pady=10)

      # Affiche la valeur actuelle
      Ajust.etiquette3 = tk.Label(fenetre, text=f"Valeur sélectionnée : {slider3.get()}")
      Ajust.etiquette3.pack(pady=10)

      # Lance la boucle de l'interface

     """

   def Lowpass():
    print ('Passe bassss')

    fenetre2 = tk.Tk()
    fenetre2.title("Reglage Chorus")

      # Crée un slider de 0 à 1
    slider4 = tk.Scale(
         fenetre2,
         from_=0,                 # Valeur minimale
         to=1000,
         resolution=100,                  # Valeur maximale
         orient="horizontal",     # Curseur horizontal
         label="cutOff",
         command=Ajust3.afficher_valeur4
         )
    slider4.pack(padx=20, pady=10)

      # Affiche la valeur actuelle
    Ajust3.etiquette4 = tk.Label(fenetre2, text=f"Valeur sélectionnée : {slider4.get()}")
    Ajust3.etiquette4.pack(pady=10)

       # Crée un slider de 0.01 à 1
    slider5 = tk.Scale(
         fenetre2,
         from_=1,                 # Valeur minimale
         to=4,
         resolution=1,                  # Valeur maximale
         orient="horizontal",     # Curseur horizontal
         label="Ordre",
         command=Ajust3.afficher_valeur5
         )
    slider5.pack(padx=20, pady=10)


    # Affiche la valeur actuelle
    Ajust3.etiquette5 = tk.Label(fenetre2, text=f"Valeur sélectionnée : {slider5.get()}")
    Ajust3.etiquette5.pack(pady=10)


    """

     # Crée un slider de 0 à 1
    slider6 = tk.Scale(
         fenetre2,
         from_=0,                 # Valeur minimale
         to=1,
         resolution=0.25,                  # Valeur maximale
         orient="horizontal",     # Curseur horizontal
         label="Balance",
         command=Ajust.afficher_valeur3
         )
    slider6.pack(padx=20, pady=10)

      # Affiche la valeur actuelle
    Ajust.etiquette3 = tk.Label(fenetre2, text=f"Valeur sélectionnée : {slider6.get()}")
    Ajust.etiquette3.pack(pady=10)

      # Lance la boucle de l'interface
    """

      #fenetre.mainloop()
