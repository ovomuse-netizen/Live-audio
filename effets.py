from pyo import *
import json 


class Effets:

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



  def Reverb(self):
    
    


    with open("effets.json", "r", encoding="utf-8") as fichier:
      donnees = json.load(fichier)
   
    #print (donnees)
    print ("Nom :", donnees["nom"])
     
    reverb = Freeverb(self.mic, size= donnees["sizeReverb"], damp= donnees["dampReverb"], bal= donnees["balReverb"])
    reverb.out()

    return reverb


  def Chorus(self):

    with open("effets.json", "r", encoding="utf-8") as fichier:
      donnees = json.load(fichier)

     
    chorus = Chorus(
    input=self.mic,
    depth= donnees["depthChorus"],     # profondeur de modulation
    feedback=donnees["feedbackChorus"], # réinjection de l'effet
    bal= donnees["balChorus"]        # équilibre entre signal sec et traité
)

    # Envoi vers la sortie
    chorus.out()

    return chorus



  def Delay(self):

    with open("effets.json", "r", encoding="utf-8") as fichier:
      donnees = json.load(fichier)
 

    source = self.mic
    delayed = Delay(source, delay=donnees["delayDelay"] ,     # retard en secondes
    feedback=donnees["feedbackDelay"] ,  # niveau de réinjection
    maxdelay=donnees["maxdelayDelay"] ,  # retard maximal prévu
    mul= donnees["mulDelay"] )

    delayed.out()
   
    return delayed

  def Harmonizer(self):

   with open("effets.json", "r", encoding="utf-8") as fichier:
      donnees = json.load(fichier)


   source = self.mic  # Entrée audio
   harmonie = Harmonizer(source, transpo=donnees["tanspoHarmonizer"]).out()  # +7 demi-tons : quinte juste

   return harmonie


  def Distortion(self):

   with open("effets.json", "r", encoding="utf-8") as fichier:
      donnees = json.load(fichier)



   audio = self.mic  # entrée audio, par exemple une guitare
   distordu = Disto(audio, drive= donnees["driveDistortion"], slope=donnees["slopeDistortion"], mul=donnees["mulDistortion"]).out()

   return distordu


  def Flanger(self):
    
     with open("effets.json", "r", encoding="utf-8") as fichier:
      donnees = json.load(fichier)


     # Signal de test
     source = self.mic

     # Délai modulé entre environ 1 et 6 ms
     lfo = Sine(freq=0.25, mul=0.0025, add=0.0035)
     delayed = Delay(
         source,
         delay=lfo,
         feedback=donnees["feedbackFlanger"],
         maxdelay=donnees["maxdelayFlanger"]
          )

     # Mélange du signal direct et du signal retardé
     flanger = source + delayed
     flanger.out()


     return flanger

  def Equaliseur(self):
 
     with open("effets.json", "r", encoding="utf-8") as fichier:
      donnees = json.load(fichier)



     source = self.mic

     # Fréquences centrales des trois bandes
     graves = Biquad(source, freq=120, q=0.8, type=2)
     mediums = Biquad(source, freq=1000, q=0.8, type=2)
     aigus = Biquad(source, freq=6000, q=0.8, type=2)

     # Gains linéaires : 1 = niveau inchangé
     gain_graves = Sig(1.0)
     gain_mediums = Sig(1.0)
     gain_aigus = Sig(1.0)

     # Mélange des bandes filtrées
     sortie = (
          graves * gain_graves
          + mediums * gain_mediums
          + aigus * gain_aigus
           ).out()

     return sortie

  def Lowpass(self):

   with open("effets.json", "r", encoding="utf-8") as fichier:
      donnees = json.load(fichier)


   source = self.mic
   filtre = ButLP(source, freq=donnees["freqLowpass"] , order=donnees["orderLowpass"])

   filtre.out()

   return filtre



