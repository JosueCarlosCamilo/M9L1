import pyttsx3

def hablar(texto):
    motor = pyttsx3.init()
    motor.setProperty('rate', 130)
    motor.say(texto)
    motor.runAndWait()
    motor.stop()

frase_inicial = "Hola, dime cómo te sientes hoy. Elige una opción: uno feliz, dos triste, tres cansado."
hablar(frase_inicial)
# Luego mostrar opciones en consola
print("¿Cómo te sientes hoy?")
print("1. Feliz ")
print("2. Triste ")
print("3. Cansado ")
print("4. Sorprendido")

estado = input("Escribe el número de tu estado de animo")

# Escoger mensaje
if estado == "1":
    mensaje = "¡Me alegra que estés feliz! Sigue disfrutando tu día."
elif estado == "2":
    mensaje = "Recuerda que después de la lluvia, siempre sale el sol."
elif estado == "3":
    mensaje = "Respira profundo. A veces descansar también es avanzar."
elif estado == "4":
    mensaje = "Estas muy maravillado con lo que has visto, fue algo feliz"
else:
    mensaje = "No entendí tu respuesta, pero te deseo un buen día."
hablar(mensaje)