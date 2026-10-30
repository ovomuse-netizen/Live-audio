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


class Ajust2():
 




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
      Ajust2.etiquette.config(text=f"Valeur sélectionnée : {valeur}")
      with open("effets.json", "r", encoding="utf-8") as fichier:
        donnees = json.load(fichier)
      if (int(valeur)<= 1):
       donnees["driveDistortion"] = float(valeur)
      else : donnees["driveDistortion"] = 1

      
      with open("effets.json", "w", encoding="utf-8") as fichier:
        json.dump(donnees, fichier, ensure_ascii=False, indent=2)
       
        ef = Effets()

        disto = ef.Distortion()


      


   def afficher_valeur2(valeur):
      Ajust2.etiquette2.config(text=f"Valeur sélectionnée : {valeur}")
      with open("effets.json", "r", encoding="utf-8") as fichier:
        donnees = json.load(fichier)
      if (float(valeur) <= 1):
        donnees["slopeDistortion"] = float(valeur)
      else : donnees["slopeDistortion"] = 1

      with open("effets.json", "w", encoding="utf-8") as fichier:
        json.dump(donnees, fichier, ensure_ascii=False, indent=2)

        ef = Effets()

        disto = ef.Distortion()



   def afficher_valeur3(valeur):
      Ajust2.etiquette3.config(text=f"Valeur sélectionnée : {valeur}")
      with open("effets.json", "r", encoding="utf-8") as fichier:
        donnees = json.load(fichier)
      if (float(valeur) <= 1):
        donnees["mulDistortion"] = float(valeur)
      else : donnees["mulDistortion"] = 1

      
      with open("effets.json", "w", encoding="utf-8") as fichier:
        json.dump(donnees, fichier, ensure_ascii=False, indent=2)

        ef = Effets()

        disto = ef.Distortion()






 # Fonction appelée quand la valeur change
   def afficher_valeur4(valeur):
      Ajust2.etiquette4.config(text=f"Valeur sélectionnée : {valeur}")
      with open("effets.json", "r", encoding="utf-8") as fichier:
        donnees = json.load(fichier)
      if (float(valeur) <= 1):
        donnees["feedbackFlanger"] = float(valeur)
      else : donnees["feedbackFlanger"] = 1

      
      with open("effets.json", "w", encoding="utf-8") as fichier:
        json.dump(donnees, fichier, ensure_ascii=False, indent=2)

        ef = Effets()

        flange = ef.Flanger()


# Fonction appelée quand la valeur change
   def afficher_valeur5(valeur):
      Ajust2.etiquette5.config(text=f"Valeur sélectionnée : {valeur}")
      with open("effets.json", "r", encoding="utf-8") as fichier:
        donnees = json.load(fichier)
      if (float(valeur) <= 0.1):
        donnees["maxdelayFlanger"] = float(valeur)
      else : donnees["maxdelayFlanger"] =0.1

      
      with open("effets.json", "w", encoding="utf-8") as fichier:
        json.dump(donnees, fichier, ensure_ascii=False, indent=2)

        ef = Effets()

        flange = ef.Flanger()

   """
# Fonction appelée quand la valeur change
   def afficher_valeur6(valeur):
      Ajust2.etiquette4.config(text=f"Valeur sélectionnée : {valeur}")
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











   def Distortion():

      
      fenetre = tk.Tk()
      

      fenetre.title("Reglage Distortion")

      # Crée un slider de 1 à 3
      slider = tk.Scale(
         fenetre,
         from_=0,                 # Valeur minimale
         to=1,
         resolution=0.1,                  # Valeur maximale
         orient="horizontal",     # Curseur horizontal
         label="Drive",
         command=Ajust2.afficher_valeur
         )
      slider.pack(padx=20, pady=10)

      # Affiche la valeur actuelle
      Ajust2.etiquette = tk.Label(fenetre, text=f"Valeur sélectionnée : {slider.get()}")
      Ajust2.etiquette.pack(pady=10)

       # Crée un slider de 0.01 à 1
      slider2 = tk.Scale(
         fenetre,
         from_=0.0,                 # Valeur minimale
         to=1,                 
         resolution=0.1,                  # Valeur maximale
         orient="horizontal",     # Curseur horizontal
         label="Slope",
         command=Ajust2.afficher_valeur2
         )
      slider2.pack(padx=20, pady=10)

      # Affiche la valeur actuelle
      Ajust2.etiquette2 = tk.Label(fenetre, text=f"Valeur sélectionnée : {slider2.get()}")
      Ajust2.etiquette2.pack(pady=10)

       # Crée un slider de 0 à 1
      slider3 = tk.Scale(
         fenetre,
         from_=0,                 # Valeur minimale
         to=1,
         resolution=0.1,                  # Valeur maximale
         orient="horizontal",     # Curseur horizontal
         label="Mul",
         command=Ajust2.afficher_valeur3
         )
      slider3.pack(padx=20, pady=10)

      # Affiche la valeur actuelle
      Ajust2.etiquette3 = tk.Label(fenetre, text=f"Valeur sélectionnée : {slider3.get()}")
      Ajust2.etiquette3.pack(pady=10)

      # Lance la boucle de l'interface



   def Flanger():
    print ('flangerrrr')

    fenetre2 = tk.Tk()
    fenetre2.title("Reglage Flanger")

      # Crée un slider de 0 à 1
    slider4 = tk.Scale(
         fenetre2,
         from_=0,                 # Valeur minimale
         to=1,
         resolution=0.1,                  # Valeur maximale
         orient="horizontal",     # Curseur horizontal
         label="Depth",
         command=Ajust2.afficher_valeur4
         )
    slider4.pack(padx=20, pady=10)

      # Affiche la valeur actuelle
    Ajust2.etiquette4 = tk.Label(fenetre2, text=f"Valeur sélectionnée : {slider4.get()}")
    Ajust2.etiquette4.pack(pady=10)

       # Crée un slider de 0.01 à 1
    slider5 = tk.Scale(
         fenetre2,
         from_=0.001,                 # Valeur minimale
         to=0.01,
         resolution=0.001,                  # Valeur maximale
         orient="horizontal",     # Curseur horizontal
         label="Max Delay",
         command=Ajust2.afficher_valeur5
         )
    slider5.pack(padx=20, pady=10)


    # Affiche la valeur actuelle
    Ajust2.etiquette5 = tk.Label(fenetre2, text=f"Valeur sélectionnée : {slider5.get()}")
    Ajust2.etiquette5.pack(pady=10)

    """
     # Crée un slider de 0 à 1
    slider6 = tk.Scale(
         fenetre2,
         from_=0,                 # Valeur minimale
         to=1,
         resolution=0.25,                  # Valeur maximale
         orient="horizontal",     # Curseur horizontal
         label="Balance",
         command=Ajust2.afficher_valeur3
         )
    slider6.pack(padx=20, pady=10)

      # Affiche la valeur actuelle
    Ajust2.etiquette3 = tk.Label(fenetre2, text=f"Valeur sélectionnée : {slider6.get()}")
    Ajust2.etiquette3.pack(pady=10)

      # Lance la boucle de l'interface

   """
      #fenetre.mainloop()
