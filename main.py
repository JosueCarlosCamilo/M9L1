import pyttsx3

#Iniciar el motor
engine = pyttsx3.init()

#configuraciones de parametros
engine.setProperty('rate', 150)#setProperty Maneja las propiedades que tiene nuestra voz de la computadora volumen y velocidad de la voz
engine.setProperty('volumen', 0.9)

voices = engine.getProperty('voices')#get.Propertytraer todas las voces
'''for i, voz in enumerate(voices):
    print(f"Voz {i}: {voz.name} - ID: {voz.id}")'''

engine.setProperty('voice', voices[0].id)

text = "Hola Camilo, espero que tengas un bello día, como estas hoy"

#Vocalizar el texto
engine.say(text)
engine.runAndWait()
