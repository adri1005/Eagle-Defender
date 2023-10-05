from tkinter import *
import sqlite3
from tkinter import filedialog
import shutil
global users
users = 0
import tkinter as tk
from pydub import AudioSegment
import sutil
from mutagen.mp3 import MP3
import pygame
import os
pygame.init()

# Directorio donde se guardarán las canciones
directorio_canciones = 'Canciones'

# Lista de canciones cargadas
canciones_cargadas = []


    
def exitt():
    pygame.mixer.music.stop()
    window.destroy()



def ventana_principal():
    global window

    window = Tk()
    window.geometry("900x700")
    window.resizable(width=False,height=False )
    canva1=Canvas(window, width= 900, height= 700)
    canva1.pack()

    Tanque=PhotoImage(file="Imágenes/Tanque.png")
    Tanque_etiqueta=canva1.create_image(450,400,image=Tanque) 
    
    EXIT=PhotoImage(file="Imágenes/BOTON SALIR.png")
    b3 = Button(window, width=EXIT.width(),height=EXIT.height(),image=EXIT, command=exitt)
    b3.place(x=0 , y=0)
    
    def reproducir_mp3():
        carpeta = "Canciones"
    # Verifica si la carpeta existe
        if os.path.exists(carpeta):
            # Encuentra todos los archivos .mp3 en la carpeta
            archivos_mp3 = [archivo for archivo in os.listdir(carpeta) if archivo.endswith('.mp3')]
            
            if archivos_mp3:
                # Muestra una lista de archivos .mp3 al cliente
                seleccion = tk.Tk()
                seleccion.title("Seleccionar archivo .mp3")
                
                lista = tk.Listbox(seleccion)
                lista.pack()
                
                for archivo in archivos_mp3:
                    lista.insert(tk.END, archivo)
                
                def reproducir_seleccion():
                    # Obtiene el archivo seleccionado
                    indice = lista.curselection()[0]
                    archivo_seleccionado = archivos_mp3[indice]
                    
                    # Reproduce el archivo seleccionado con pygame
                    pygame.mixer.init()
                    pygame.mixer.music.load(os.path.join(carpeta, archivo_seleccionado))
                    pygame.mixer.music.play()
                    
                boton_reproducir = tk.Button(seleccion, text="Reproducir", command=reproducir_seleccion)
                boton_reproducir.pack()
                
                seleccion.mainloop()
            else:
                print("No se encontraron archivos .mp3 en la carpeta.")
        else:
            print("La carpeta especificada no existe.")
    
    # Especifica la dirección de la carpeta que deseas utilizar


    
    btn_cargar = tk.Button(window , text="Elegir Canción", command=reproducir_mp3)

    playbtn = Button(width=15,height=3,text="PLAY",command=openplayscreen)
    playbtn.place(x=450,y=350)
    btn_cargar.place(x=450,y=500)


    window.mainloop()
    



def gamewindow():
    def exittt():
        pygame.mixer.music.stop()
        ventana.destroy()
    
    # Tamaño del mapa
    mapa_ancho = 1200
    mapa_alto = 1500

    # Tamaño de cada cuadrado imaginario
    cuadrado_lado = 65.5

    # Inicialización de cuadrados
    #cuadrados_libres = set()

    # Crear ventana
    ventana = tk.Tk()
    ventana.title("Mapa Cuadriculado")

    # Crear lienzo
    canvas = tk.Canvas(ventana, width=mapa_ancho, height=mapa_alto)
    canvas.pack()
    woodenblock = PhotoImage(file="D:/TEC/pRINCIPIOS/Imágenes/woodenblock.png")
    Tanque=PhotoImage(file="D:/TEC/pRINCIPIOS/Imágenes/FONDO.png")
    Tanque_etiqueta=canvas.create_image(450,400,image=Tanque)
    
    EXIT=PhotoImage(file="Imágenes/BOTON SALIR.png")
    b3 = Button(ventana, width=EXIT.width(),height=EXIT.height(),image=EXIT, command=exittt)
    b3.place(x=0 , y=0)

    #def crear_cuadricula():
        #pass

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

    #crear_cuadricula()
    canvas.bind("<Button-1>", colocar_bloque)

    ventana.mainloop()


def openplayscreen():
    global window
    window.destroy()
    gamewindow()










