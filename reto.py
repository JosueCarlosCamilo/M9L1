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
print("5. Asustado")
estado = input("Escribe el número de tu estado de animo")

# Escoger mensaje
if estado == "1":
    mensaje = "¡Me alegra que estés feliz! Sigue disfrutando tu día."
elif estado == "2":
    mensaje = "Recuerda que después de la lluvia, siempre sale el sol."
elif estado == "3":
    mensaje = "Respira profundo. A veces descansar también es avanzar."
elif estado == "4":
    mensaje = "Estas muy maravillado con lo que has visto, ¿fue algo feliz?"
elif estado == "5":
    mensaje = "Calmate cuenta 1 2 3, respira, lentamente"
else:
    mensaje = "No entendí tu respuesta, pero te deseo un buen día."
hablar(mensaje)
despues = input("Continua con el número que escogiste")

if despues == "1":
    continuando = ("Cuentame, de que estas feliz")
elif despues == "2":
    continuando = ("Ya estas más tranquilo")
elif despues == "3":
    continuando = ("Y te sientes más Relajado")
elif despues == "4":
    continuando = ("Que fue lo que te encanto")      
elif despues == "5":
    continuando = ("Ahora sal afuera y relajate o descansa un poco")
else:
    continuando = "no entendi tu mensaje"
hablar(continuando)
despues = input("Continua con el número que escogiste")

if despues == "1":
    mensaje = "Quieres una recomendación"
elif despues == "2":
    mensaje = "Has un ejercicio solo 5 actos"
elif despues == "3":
    mensaje = "Sal afuera un minuto"
elif despues == "4":
    mensaje == "No te olvides que es lo que te relaja y nunca lo descuides, pero no te satures en tu día"
elif despues == "5":
    mesaje = "Sirvete un cafe o te y celebra cuando lo hayas hecho y cuando lo termines celebratelo tambien, sirvete de nuevo si quieres pero continua con este proceso solo viendo tus acciones a partir de decidir hacerlo"
else:
    mensaje = "Por favor escribelo de nuevo"
hablar(mensaje)


