import random
def juego_adivinanza():
    numero_secreto = random.randint(1, 100)

    intentos = 0
    adivinando  = False

    print("Bien venido al juego de adivinanza de numeros")
    print("Debes adivinar un numero entre el 1 al 100")
    print("¡Intenta adivinarlo!")

    while not adivinando:

        adivinanza = input("Intrudusaca un numero del 1 al 100:")

        if adivinanza.isdigit():
            adivinanza = int(adivinanza)
            intentos += 1

            if adivinanza < numero_secreto:
                print(f"El numero secreto es mayor a {adivinanza} ")
            elif adivinanza > numero_secreto:
                 print(f"El numero es menor a {adivinanza}")
            else:
           
                print(f"¡Felicitaciones has ganado¡")
        else:
            print("Por favor intudusca un numero")
            
juego_adivinanza()