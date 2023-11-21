import factoria
if __name__ == '__main__':
     mi_genero = input("Seleccione F/M: ")[0]
     mi_nombre = input("Nombre: ")
     mi_edad = input("edad: ")
     mi_factoria = factoria.Factoria()
     #Factoria, crea a una persona!
     persona = mi_factoria.get_persona(mi_nombre, mi_genero, mi_edad)
 #se ha creado una persona