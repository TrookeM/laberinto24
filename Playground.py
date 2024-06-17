from LaberintoBuilder.Director import Director
from Ente.Character import Character
import os
import sys

# Para evitar errores de recursión
nombre = input("Nick del personaje: ")
personaje = Character()

opcion = input("Opción de juego:\n    1. Jugar\n    2. Salir\nSelecciona una opción: ")

jsons = os.listdir('json/')
print("JSON disponibles:")
for idx, json_file in enumerate(jsons):
    print(f"    {idx}. {json_file}")

while opcion not in ["1", "2"]:
    print("Opción inválida. Por favor, selecciona una opción válida (1 o 2).")
    opcion = input("Opción de juego:\n    1. Jugar\n    2. Salir\nSelecciona una opción: ")

if opcion == "2":
    sys.exit()

json_idx = input("Selecciona un json: ")
while not json_idx.isdigit() or int(json_idx) < 0 or int(json_idx) >= len(jsons):
    print("Selección inválida. Introduce un número válido correspondiente al JSON.")
    json_idx = input("Selecciona un json: ")

json_file = jsons[int(json_idx)]

director = Director()
director.procesar(os.path.join('json', json_file))
juego = director.getJuego()
forma = director.form
personaje.seudonimo = nombre
juego.agregarPersonaje(personaje)
juego.prota = personaje
print(forma)

while not juego.fase.esFinal():
    if forma == "Cuadrado":
        print("\n¿Qué deseas hacer?\n    A. Atacar\n    1. Mover al norte\n    2. Mover al este\n    3. Mover al oeste\n    4. Mover al sur\n",
              "   5. Abrir Puertas\n    6. Lanzar bichos\n    7. Mostrar comandos bolsa\n    8. Mostrar comandos cuerpo\n",   
              "   H. Obtener objetos de la posición del personaje\n    C. Obtener Comandos\n    I. Mostrar inventario")
    elif forma == "Diamante":
        print("\n¿Qué deseas hacer?\n    A. Atacar\n    1. Mover al noreste\n    2. Mover al noroeste\n    3. Mover al sureste\n    4. Mover al suroeste\n",
              "   5. Abrir Puertas\n    6. Lanzar bichos\n    7. Mostrar comandos bolsa\n    8. Mostrar comandos cuerpo\n",
              "   H. Obtener objetos de la posición del personaje\n    C. Obtener Comandos\n    I. Mostrar inventario")
    elif forma == "Triangulo":
        print("\n¿Qué deseas hacer?\n    A. Atacar\n    1. Mover al norte\n    2. Mover al este\n    3. Mover al oeste\n",
              "   4. Abrir Puertas\n    5. Lanzar bichos\n    6. Mostrar comandos bolsa\n    7. Mostrar comandos cuerpo\n",
              "   H. Obtener objetos de la posición del personaje\n    C. Obtener Comandos\n    I. Mostrar inventario")

    sys.stdin.flush()
    eleccion = input("Ingresa tu elección: ")

    if eleccion == "1":
        if forma == "Cuadrado":
            personaje.irAlNorte()
        elif forma == "Diamante":
            personaje.irAlNoreste()
        elif forma == "Triangulo":
            personaje.irAlNorte()

    elif eleccion == "2":
        if forma == "Cuadrado":
            personaje.irAlEste()
        elif forma == "Diamante":
            personaje.irAlNoroeste()
        elif forma == "Triangulo":
            personaje.irAlEste()

    elif eleccion == "3":
        if forma == "Cuadrado":
            personaje.irAlOeste()
        elif forma == "Diamante":
            personaje.irAlSureste()
        elif forma == "Triangulo":
            personaje.irAlOeste()

    elif eleccion == "4":
        if forma == "Cuadrado":
            personaje.irAlSur()
        elif forma == "Diamante":
            personaje.irAlSuroeste()
        else:
            juego.openDoors() # Si es triangulo la opcion es abrir puertas

    elif eleccion == "5":
        if forma == "Triangulo":
            juego.fabricarBichoAgresivo(2)
        else:
            juego.openDoors()

    elif eleccion == "6":
        if forma == "Triangulo":
            coms = personaje.mochila.obtenerComandos(personaje)
            if len(coms) > 0:
                print("Comandos disponibles:")
                for idx, com in enumerate(coms):
                    print(f"    {idx}. {com}")
                el = input("Selecciona un comando (número): ")
                while not el.isdigit() or int(el) < 0 or int(el) >= len(coms):
                    print("Selección inválida. Introduce un número válido correspondiente al comando.")
                    el = input("Selecciona un comando (número): ")
                coms[int(el)].ejecutar(personaje)
            else:
                print("No hay objetos en la bolsa.")
        else:
            juego.fabricarBichoAgresivo(2)

    elif eleccion == "7":
        if forma == "Triangulo":
            print("¿De verdad quieres usar el brazo ataque?")
            respuesta = input("1. Sí\nCualquier otra tecla para cancelar: ")
            if respuesta == "1":
                if personaje.cuerpo.brazoAtaque is not None:
                    coms = personaje.cuerpo.brazoAtaque.commmands
                    if len(coms) > 0:
                        print("Comandos disponibles:")
                        for idx, com in enumerate(coms):
                            print(f"    {idx}. {com}")
                        el = input("Selecciona un comando (número): ")
                        while not el.isdigit() or int(el) < 0 or int(el) >= len(coms):
                            print("Selección inválida. Introduce un número válido correspondiente al comando.")
                            el = input("Selecciona un comando (número): ")
                        coms[int(el)].ejecutar(personaje)
                    else:
                        print("No hay comandos disponibles para el brazo de ataque.")
                else:
                    print("No hay nada en la mano derecha.")
        else:
            coms = personaje.mochila.obtenerComandos(personaje)
            if len(coms) > 0:
                print("Comandos disponibles:")
                for idx, com in enumerate(coms):
                    print(f"    {idx}. {com}")
                el = input("Selecciona un comando (número): ")
                while not el.isdigit() or int(el) < 0 or int(el) >= len(coms):
                    print("Selección inválida. Introduce un número válido correspondiente al comando.")
                    el = input("Selecciona un comando (número): ")
                coms[int(el)].ejecutar(personaje)
            else:
                print("No hay objetos en la bolsa.")

    elif eleccion.lower() == "a":
        personaje.atacar()

    elif eleccion.lower() == "i":
        print("Inventario:")
        if len(personaje.mochila.children) > 0:
            for idx, obj in enumerate(personaje.mochila.children):
                print(f"    {idx}. {obj}")
            el = input("Selecciona un objeto (número): ")
            while not el.isdigit() or int(el) < 0 or int(el) >= len(personaje.mochila.children):
                print("Selección inválida. Introduce un número válido correspondiente al objeto.")
                el = input("Selecciona un objeto (número): ")
            
            coms = personaje.mochila.children[int(el)].obtenerComandos(personaje)
            if len(coms) > 0:
                print("Comandos disponibles:")
                for idx, com in enumerate(coms):
                    print(f"    {idx}. {com}")
                ele = input("Selecciona un comando (número): ")
                while not ele.isdigit() or int(ele) < 0 or int(ele) >= len(coms):
                    print("Selección inválida. Introduce un número válido correspondiente al comando.")
                    ele = input("Selecciona un comando (número): ")
                coms[int(ele)].ejecutar(personaje)
            else:
                print("No hay comandos disponibles para este objeto.")
        else:
            print("No hay objetos en la mochila.")

    elif eleccion.lower() == "h":
        hijos = juego.getChildrenPosition()
        if len(hijos) > 0:
            print("Objetos disponibles:")
            for idx, hijo in enumerate(hijos):
                print(f"    {idx}. {hijo}")
            el = input("Selecciona un objeto (número): ")
            while not el.isdigit() or int(el) < 0 or int(el) >= len(hijos):
                print("Selección inválida. Introduce un número válido correspondiente al objeto.")
                el = input("Selecciona un objeto (número): ")
            hijos[int(el)].entrar(personaje)
        else:
            print("No hay objetos en la sala.")

    elif eleccion.lower() == "c":
        coms = personaje.obtenerComandos(personaje)
        if len(coms) > 0:
            print("Comandos disponibles:")
            for idx, com in enumerate(coms):
                print(f"    {idx}. {com}")
            el = input("Selecciona un comando (número): ")
            while not el.isdigit() or int(el) < 0 or int(el) >= len(coms):
                print("Selección inválida. Introduce un número válido correspondiente al comando.")
                el = input("Selecciona un comando (número): ")
            coms[int(el)].ejecutar(personaje)
        else:
            print("No hay comandos disponibles.")
