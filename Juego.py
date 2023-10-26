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

global CancionAtacante
CancionAtacante=""

global CancionDefensor
CancionDefensor=""
    
from Utils import user1 , user2 



def ventana_principal():
    
        
    global CancionAtacante
    
    window = Tk()
    window.geometry("1025x1015")
    canva1=Canvas(window, width= 1045, height= 1015)
    canva1.pack()
    
    Tanque=PhotoImage(file="Imágenes/Fondo juego.png")
    EXIT=PhotoImage(file="Imágenes/BotonSalirMenu.png")
    pp=PhotoImage(file="Imágenes/FondoRank4.png")
    Play=PhotoImage(file="Imágenes/JugarBoton (1) (1).png")
    MusicB=PhotoImage(file="Imágenes/MusicaBoton (1).png")
    RankingB = PhotoImage(file="Imágenes/RankingBoton (1).png")
    AyudaB = PhotoImage(file="Imágenes/AyudaBoton (1).png")
    InfoB = PhotoImage(file="Imágenes/InfoBoton (1).png")
    ConfigB=PhotoImage(file="Imágenes/ConfigBoton (1) (1).png")
    a=PhotoImage(file="Imágenes/FONDOBOT (1).png")
    volverRank=PhotoImage(file="Imágenes/BotonSalirRank.png")
    FondoInfo=PhotoImage(file="Imágenes/+InfoFondo.png")
    FondoMusic=PhotoImage(file="Imágenes/FondoMusic.png")
    BotMusAta=PhotoImage(file="Imágenes/BotonMusicAta.png")
    BotMusDef=PhotoImage(file="Imágenes/BotonMusicdef.png")
    AgC=PhotoImage(file="Imágenes/Ag1-removebg-preview.png")
    TaC=PhotoImage(file="Imágenes/ta1-removebg-preview.png")
    Control=PhotoImage(file="Imágenes/Control (1).png")
    FondoConfig=PhotoImage(file="Imágenes/FondoConfig.png")
    BotRoles=PhotoImage(file="Imágenes/BotonRoles.png")
    def submenu():    
        window.geometry("1025x1015")
        canva1.config(width=1025, height=1015)#se configura el canvas
        canva1.create_image(0, 0, anchor=tk.NW, image=Tanque)
        
        
        
        background_color_hex = "#fcf3b8"
        rosa ="#d84cff"
        verde="#32e800"
        rojo="#f90000"
        negro="#000000"
        cian="#429083"
        blood="#560001"
       
        def exitt():
            pygame.mixer.music.stop()
            window.destroy()
        
        
            
            # Botón para seleccionar el usuario
            boton_seleccionar = tk.Button(window, text="Seleccionar Usuario", command=seleccionar_usuario)
            boton_seleccionar.pack()

        def back():#comando para volver al submenu
            canva1.delete("all")
            submenu()
            
        def ventana_rank():
            window.geometry("880x1015")
            canva1.config(width=880, height=1015)#se configura el canvas
            canva1.delete("all")
            
            
            canva1.create_image(0, 0, anchor=tk.NW, image=pp)
            
            RankingVolver = Button(canva1,width=volverRank.width(),height=volverRank.height(),image=volverRank,command = back ,bg="black")
            canva1.create_window(30,50,window= RankingVolver)
            
            # Leer el archivo de texto
            with open("Ranking.txt", "r") as file:
                lines = file.readlines()

            # Crear una lista de tuplas (puntaje, nombre) a partir de las líneas
            scores = []
            for line in lines:
                line = line.strip()
                if line:
                    import re
                    match = re.match(r'\[\[(\d+)\]\[(\w+)\]\]', line)
                    if match:
                        score = int(match.group(1))
                        name = match.group(2)
                        scores.append((score, name))

            # Ordenar la lista de tuplas por puntaje en orden descendente
            sorted_scores = sorted(scores, key=lambda x: x[0], reverse=True)

            # Tomar los 5 mejores puntajes
            top_scores = sorted_scores[:4]



            # Mostrar los 5 mejores puntajes en el canvas
            for i, (score, name) in enumerate(top_scores, start=1):
                text = f"{i}. {name}: {score}"
                canva1.create_text(10, 330+ i*93, text=text, anchor="w", font = ("Arial", 25))
                
        def ventana_music():
            window.geometry("1024x1015")
            canva1.config(width=1024, height=1015)#se configura el canvas
            canva1.delete("all")
            
            canva1.create_image(0, 0, anchor=tk.NW, image=FondoMusic)
            
            RankingVolver = Button(canva1,width=volverRank.width(),height=volverRank.height(),image=volverRank,command = back ,bg="black")
            canva1.create_window(30,984,window= RankingVolver)
            
            BotMusDefe = Button(canva1,width= BotMusDef.width(),height= BotMusDef.height(),image= BotMusDef,command = reproducir_mp3Def ,bg="black")
            canva1.create_window(245,69,window= BotMusDefe)
            
            BotMusAtac = Button(canva1,width=BotMusAta.width(),height=BotMusAta.height(),image=BotMusAta,command = reproducir_mp3 ,bg="black")
            canva1.create_window(761,950,window= BotMusAtac)
        
        def ventana_config():
            window.geometry("1024x1015")
            canva1.config(width=1024, height=1015)#se configura el canvas
            canva1.delete("all")
            def elegirRol():
                global user1
                global user2
                # Función que se ejecutará cuando se haga clic en un botón para seleccionar el usuario
                def seleccionar_usuario():
                    seleccion = lista_usuarios.get(lista_usuarios.curselection())  # Obtiene el elemento seleccionado
                    print("Usuario seleccionado:", seleccion)

                # Crear una ListBox con los nombres de usuario
                lista_usuarios = tk.Listbox(window)
                lista_usuarios.insert(1, user1)
                lista_usuarios.insert(2, user2)
                lista_usuarios.pack()
            
            canva1.create_image(0, 0, anchor=tk.NW, image=FondoConfig)
            
            Roles = Button(canva1,width=BotRoles.width(),height=BotRoles.height(),image=BotRoles,command =elegirRol ,bg="black")
            canva1.create_window(520,304,window= Roles)
            
            
            
            
        def ventana_info():
            window.geometry("980x1015")
            canva1.config(width=980, height=1015)#se configura el canvas
            canva1.delete("all")
            
            canva1.create_image(0, 0, anchor=tk.NW, image=FondoInfo)
            
            RankingVolver = Button(canva1,width=volverRank.width(),height=volverRank.height(),image=volverRank,command = back ,bg="black")
            canva1.create_window(30,40,window= RankingVolver)
            
            canva1.create_text(525, 420, text=" Los juegos retro se han vuelto cada vez más populares \n En los últimos años, estos juegos se caracterizan por \n tener gráficos y sonidos simples, y por ser fáciles de \n jugar. \n Ahora por solicitud de un grupo de aficionados \n  de juegos retro llamado “Los 80´s Players”, se ha creado \n esta versión de uno de los ejemplares más famoso  \n de este tipo de videojuegos, el cual se titula: \n “Eagle Defender”. \n En este juego un jugador tiene la labor de \n destruir un águila y el otro la debe de defender, por lo \n que se deben implementar estas funcionalidades, además \n de otras para hacer el juego más entretenido y ameno.", font=("Helvetica", 15), fill="black")
            
            canva1.create_text(490,60, text="           Autores: \n Adrián Muñoz Alvarado \n Diego Salas Ovares \n Gabriel Fernández Vargas \n Leandro Ruiz Acuña", font=("Helvetica", 16),fill= background_color_hex)
        
        def ventana_ayuda():
            window.geometry("1800x1100")
            canva1.config(width=1800, height=1100)#se configura el canvas
            canva1.delete("all")
            
            canva1.create_image(550, 20, anchor=tk.NW, image=Control)
            canva1.create_image(10, 700, anchor=tk.NW, image=AgC)
            canva1.create_image(1300, 700, anchor=tk.NW, image=TaC)
            
            
            
            RankingVolver = Button(canva1,width=volverRank.width(),height=volverRank.height(),image=volverRank,command = back ,bg="black")
            canva1.create_window(30,40,window= RankingVolver)
            
            canva1.create_text(880, 440, text="Botón rosa", font=("Helvetica", 35), fill=rosa)           
            canva1.create_text(880,520, text="Botón verde", font=("Helvetica", 35),fill= verde)
            canva1.create_text(880,600, text="Botón rojo", font=("Helvetica", 35),fill= rojo)
            canva1.create_text(880,680, text="Botón negro", font=("Helvetica", 35),fill= negro)
            
            canva1.create_text(200, 440, text="Colocar bloque de madera", font=("Helvetica", 25), fill=cian)    
            canva1.create_text(200, 520, text="Colocar bloque de concreto", font=("Helvetica", 25), fill=cian) 
            canva1.create_text(200, 600, text="Colocar bloque de acero", font=("Helvetica", 25), fill=cian) 
            canva1.create_text(200, 680, text="Seleccionar/Recoger bloque", font=("Helvetica", 25), fill=cian) 
            
            canva1.create_text(1600, 440, text="Disparar bola de agua", font=("Helvetica", 25), fill=blood)    
            canva1.create_text(1600, 520, text="Disparar bola de fuego", font=("Helvetica", 25), fill=blood) 
            canva1.create_text(1600, 600, text="Disparar bomba", font=("Helvetica", 25), fill=blood) 
            canva1.create_text(1590, 680, text="Seleccionar/Pausar la partida", font=("Helvetica", 25), fill=blood)
        
        def reproducir_mp3():
            global CancionAtacante
            global CancionDefensor
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
                        CancionAtacante=archivo_seleccionado
                        print(CancionAtacante)
                        
                        # Reproduce el archivo seleccionado con pygame
                        """pygame.mixer.init()
                        pygame.mixer.music.load(os.path.join(carpeta, archivo_seleccionado))
                        pygame.mixer.music.play()"""
                        
                    boton_reproducir = tk.Button(seleccion, text="Reproducir", command=reproducir_seleccion)
                    boton_reproducir.pack()
                    
                    seleccion.mainloop()
                else:
                    print("No se encontraron archivos .mp3 en la carpeta.")
            else:
                print("La carpeta especificada no existe.")
        
        # Especifica la dirección de la carpeta que deseas utilizar
        def reproducir_mp3Def():
            global CancionAtacante
            global CancionDefensor
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
                        CancionDefensor = archivo_seleccionado
                        print(CancionDefensor)
                        
                        # Reproduce el archivo seleccionado con pygame
                    """ pygame.mixer.init()
                        pygame.mixer.music.load(os.path.join(carpeta, archivo_seleccionado))
                        pygame.mixer.music.play()"""
                        
                    boton_reproducir = tk.Button(seleccion, text="Reproducir", command=reproducir_seleccion)
                    boton_reproducir.pack()
                    
                    seleccion.mainloop()
                else:
                    print("No se encontraron archivos .mp3 en la carpeta.")
            else:
                print("La carpeta especificada no existe.")
        
        # Especifica la dirección de la carpeta que deseas utilizar
    
        
        
        canva1.create_image(375,416 , anchor=tk.NW, image=a)
        canva1.create_image(375,492 , anchor=tk.NW, image=a)
        canva1.create_image(375,565 , anchor=tk.NW, image=a)
        canva1.create_image(375,642 , anchor=tk.NW, image=a)
        canva1.create_image(375,727 , anchor=tk.NW, image=a)
        canva1.create_image(375,802 , anchor=tk.NW, image=a)
        
        btn_cargar = tk.Button(window , text="Elegir Canción", command=reproducir_mp3)
        
        playbtn = Button(canva1,width=Play.width(),height=Play.height(),image=Play,command=openplayscreen,bg="black")
        canva1.create_window(492,440,window=playbtn)
        
        
        Musicbtn = Button(canva1,width=MusicB.width(),height=MusicB.height(),image=MusicB,command=ventana_music, bg="black")
        canva1.create_window(492,512,window= Musicbtn)
        
        
        Configbtn = Button(canva1,width=ConfigB.width(),height=ConfigB.height(),image=ConfigB,command=ventana_config,bg="black")
        canva1.create_window(492,670,window= Configbtn)
        
        
        Rankingbtn = Button(canva1,width=RankingB.width(),height=RankingB.height(),image=RankingB,command = ventana_rank ,bg="black")
        canva1.create_window(492,586,window= Rankingbtn)
        
        
        Ayudabtn = Button(canva1,width=AyudaB.width(),height=AyudaB.height(),image=AyudaB,command=ventana_ayuda,bg="black")
        canva1.create_window(492,750,window= Ayudabtn)
        
        
        Infobtn = Button(canva1,width = InfoB.width(),height=InfoB.height(),image=InfoB,command=ventana_info,bg="black")
        canva1.create_window(492,827,window= Infobtn)
        
        b3 = Button(canva1, bg="black", width=EXIT.width(),height=EXIT.height(),image=EXIT, command=exitt)
        canva1.create_window(33,39,window = b3)
        
    submenu()
    
        
        
        
        
       
    
       
    window.mainloop()
    


    
    
    


def gamewindow():
    def exittt():
        pygame.mixer.music.stop()
        ventana.destroy()
    
    # Tamaño del mapa
    mapa_ancho = 1183
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









