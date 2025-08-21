import os

lista_tareas = []

def leer_tareas(nombre_archivo="tareas.txt"):
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            return [linea.strip() for linea in archivo.readlines()]
    except FileNotFoundError:
        return []

def guardar_tareas(lista_tareas, nombre_archivo="tareas.txt"):
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        for tarea in lista_tareas:
            archivo.write(tarea + "\n")

def main():
    os.system('cls' if os.name == 'nt' else 'clear') #Limpia la consola
    mostrar_tareas()
    accion()

def end(): #despues de cada comando, pulsamos una tecla y carga el main
    input("Pulse Cualquier tecla para continuar...")
    main()

def mostrar_tareas():
    tareas_guardadas =leer_tareas()
    print("📋 Lista de tareas:")
    for tarea in tareas_guardadas:
        print(f"- {tarea}")
    for tarea in lista_tareas:
        print(f"- {tarea}")

def accion():
    #Lista de comandos
    print("Ingresar = add nombre_tarea, Borrar = rm nombre_tarea, Guardar = save, Salir = exit ")
    comando = input() #insertar el comando + tarea

    partes =comando.split(maxsplit=1) #Dividimos la parte del comando del nombre de la tarea
   
    if len(partes) == 2:

        operacion, tarea = partes #Asignamos la primera parte del split a operacion y la segunda a tarea
        
        #AGREGAR TAREA
        if operacion == "add":
            if tarea in lista_tareas:
                print("La tarea ya existe.")
                #Si la tarea existe en la lista, no la agrega
            else:
                lista_tareas.append(tarea)
                print("Tarea agregada correctamente.")
                #Si la tarea no existe en la lista, la agrega
        #ELIMINAR TAREA
        elif operacion == "rm":
            if tarea in lista_tareas:
                lista_tareas.remove(tarea)
                print("Tarea eliminada correctamente.")
                #Si la tarea existe en la lista, la elimina
            else:
                print("La tarea no existe")
                #Si la tarea no existe en la lista, no hace nada
    else: 
        operacion = partes[0]
        if operacion == "save":
            guardar_tareas(lista_tareas)
        elif operacion == "exit":
            exit()
        else:
            print("Comando no reconocido...")
    end()
main()
