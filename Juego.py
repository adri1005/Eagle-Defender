from tkinter import *
import tkinter as tk

def ventana_principal():
    global window

    window = Tk()
    window.geometry("900x700")
    window.resizable(width=False,height=False )
    canva1=Canvas(window, width= 900, height= 700)
    canva1.pack()

    Tanque=PhotoImage(file="Imágenes/Tanque.png")
    Tanque_etiqueta=canva1.create_image(450,400,image=Tanque)




    playbtn = Button(width=15,height=3,text="PLAY",command=openplayscreen)
    playbtn.place(x=400,y=100)
    window.mainloop()
    



def gamewindow():
    
    # Tamaño del mapa
    mapa_ancho = 1200
    mapa_alto = 1500

    # Tamaño de cada cuadrado imaginario
    cuadrado_lado = 65.5

    # Inicialización de cuadrados
    cuadrados_libres = set()

    # Crear ventana
    ventana = tk.Tk()
    ventana.title("Mapa Cuadriculado")

    # Crear lienzo
    canvas = tk.Canvas(ventana, width=mapa_ancho, height=mapa_alto)
    canvas.pack()
    woodenblock = PhotoImage(file="Imágenes/woodenblock.png")
    Tanque=PhotoImage(file="Imágenes/FONDO.png")
    Tanque_etiqueta=canvas.create_image(450,400,image=Tanque)

    def crear_cuadricula():
        pass

    cuadrados_ocupados = []

    def colocar_bloque(event):
        
        x, y = event.x, event.y
        cuadro_x = x // cuadrado_lado * cuadrado_lado
        cuadro_y = y // cuadrado_lado * cuadrado_lado
        print(f"Clic en X={x}, Y={y}, Cuadro en X={cuadro_x}, Y={cuadro_y}")
        if (cuadro_x, cuadro_y) not in cuadrados_ocupados:
            canvas.create_image(cuadro_x, cuadro_y, anchor=tk.NW, image=woodenblock)
            cuadrados_ocupados.append((cuadro_x, cuadro_y))
            ventana.update_idletasks()  # Actualizar la ventana
        else:
            print ("ocupado")

    crear_cuadricula()
    canvas.bind("<Button-1>", colocar_bloque)

    ventana.mainloop()


def openplayscreen():
    global window
    window.destroy()
    gamewindow()



ventana_principal()

# Iniciar la aplicación con la ventana de inicio
ventana_inicio()
