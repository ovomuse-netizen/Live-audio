import tkinter as tk
from tkinter.messagebox import showinfo
from tkinter import ttk
from tkinter import Tk, Button
#import pyaudio
import time
import numpy as np
from pyo import *
from effets import Effets
from ajuste import Ajust
from ajuste2 import Ajust2



# create the main window
root = tk.Tk()
root.geometry('400x380')
root.title('Listbox')





#s = Server( nchnls=1,sr=44100,buffersize=1024, duplex=1)
#self.server = Server( nchnls=1,sr=44100,buffersize=1024, duplex=1)


#s.setInputDevice(0)   # À remplacer par l'identifiant de votre entrée
#s.setOutputDevice(2)
#self.server.setOutputDevice(2)  
#s.setOutputDevice(2)   
#
#s.boot()
#self.server.boot()
#s.start()
#self.server.start()

#mic = Input() 
#mic.out()


#s.recstart()

label = tk.Label(root, text="" )
texte = tk.StringVar(value="Texte initial")
label = tk.Label(root, textvariable=texte)
label.pack(padx=20, pady=10)

#miccheck = Input()

#miccheck = Input().play().out()

#s.gui(locals())




# create a variabe object
languages = ('Chorus', 'Flanger', 'Delay', 'Distortion', 'Reverb',
         'Harmonizer','Equaliseur', 'Lowpass')

list_variable = tk.Variable(value=languages)


# label
label = ttk.Label(
    root, 
    text='Select your favorite effects:'
)
label.pack(padx=10, pady=0, side=tk.TOP, fill=tk.X)

listbox = tk.Listbox(
    root,
    listvariable=list_variable,
    height=6,
    selectmode=tk.MULTIPLE,
)

listbox.pack(padx=10, pady=10, expand=True, fill=tk.BOTH, side=tk.LEFT)


def handle_item_select(event):
    selected_indices = listbox.curselection()
    selected_languages = ",".join([listbox.get(i) for i in selected_indices])
    CHUNK = 2**11
    #s = Server().boot()
    
    select =f'{selected_languages}'
    #p = pyaudio.PyAudio()
   
    # Renvoie le signal du micro vers les haut-parleurs
    

    

    # Garde le programme actif et ouvre l'interface pyo
    # s.gui(locals())

    texte.set(f'{selected_languages}')
    #label.config(text=f"Compteur : {select}")
    """    
    showinfo(
        title='Information', 
        message=f'You selected: {selected_languages}'
    )
    """
    return '{selected_languages}'

def selectionner():
   entree = texte.get()
   ef = Effets()
   i=0
   result = entree.split(",")
   for res in result:
       i=i+1      
       if res == 'Reverb':
          reverbe = ef.Reverb()
       
       if res == 'Delay':
          delay = ef.Delay()
       if res == 'Chorus':
         chorus = ef.Chorus()
       if res == 'Distortion':
         disto = ef.Distortion()
       if res == 'Flanger':
         flange = ef.Flanger()
       if res == 'Harmonizer':
         harmo = ef.Harmonizer()
       if res == 'Equaliseur':
         equa = ef.Equaliseur()


   showinfo(
        title='Selection', 
        message=f"revve=Effets.{res}(mic)"
    )
   
def ajuste():
  
   """
   s = Server(audio="portaudio", nchnls=2, duplex=1)
   s.setOutputDevice(2)   
   s.boot()
   s.start()

   mic = Input(chnl=0) 
   """
   #mic.stop()


   entree = texte.get()
   result = entree.split(",")
   for res in result:
      if res == 'Chorus':
         chorus = Ajust.Chorus()
      if res == 'Reverb':
         reverbe = Ajust.Reverb()
      if res == 'Distortion':
         disto = Ajust2.Distortion()
      if res == 'Flanger':
         flange = Ajust2.Flanger()

root = tk.Tk()


listbox.bind('<<ListboxSelect>>' , handle_item_select)


select = tk.StringVar()
select.trace("w", handle_item_select)



showinfo(
        title='Information', 
        message=f'A été transmis: {texte}'
    )

entry = tk.Entry(root, textvariable=select)
entry.pack()
entree = texte.get()
#label.config(text=f"pourEntry : {entree}")
"""
showinfo(
        title='Information', 
        message=f'Pour Entry  {entree}'
    )
"""
button = Button(root, text="Select!", command=selectionner)
button.pack()
button2 = Button(root, text="Ajuster", command=ajuste)
button2.pack()

#reverbe = Effets.Reverb(mic)   

#s.gui(locals())

root.mainloop()

