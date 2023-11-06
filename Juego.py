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
import os
import pygame
import pygame.time
import sys
import time
pygame.init()

# Directorio donde se guardarán las canciones
directorio_canciones = 'Canciones'

# Lista de canciones cargadas
canciones_cargadas = []

global CancionAtacante
CancionAtacante="stranger-things-124008.mp3"

global CancionDefensor
CancionDefensor="creepy-devil-dance-166764.mp3"
    
from Utils import user1 , user2 

cambios = 0  # Declarar 'cambios' como una variable global


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
    FondoAyuda=PhotoImage(file="Imágenes/FondoHelp.png")
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
        blood="#fa9905"
       
        def exitt():
            window.destroy()
        
        
            


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
            sorted_scores = sorted(scores, key=lambda x: x[0], reverse=False)

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
            RankingVolver = Button(canva1,width=volverRank.width(),height=volverRank.height(),image=volverRank,command = back ,bg="black")
            canva1.create_window(30,40,window= RankingVolver)
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
            
            canva1.create_image(0, 0, anchor=tk.NW, image=FondoAyuda)
            
            canva1.create_image(550, 20, anchor=tk.NW, image=Control)
            canva1.create_image(10, 700, anchor=tk.NW, image=AgC)
            canva1.create_image(1300, 700, anchor=tk.NW, image=TaC)
            
            
            
            RankingVolver = Button(canva1,width=volverRank.width(),height=volverRank.height(),image=volverRank,command = back ,bg="black")
            canva1.create_window(30,40,window= RankingVolver)
            
            canva1.create_text(880, 440, text="Botón rosa", font=("Helvetica", 35), fill=rosa)           
            canva1.create_text(880,520, text="Botón verde", font=("Helvetica", 35),fill= verde)
            canva1.create_text(880,600, text="Botón rojo", font=("Helvetica", 35),fill= rojo)
            canva1.create_text(880,720, text="Botón negro", font=("Helvetica", 35),fill= negro)
            
            canva1.create_text(200, 440, text="Colocar bloque de madera", font=("Helvetica", 25), fill=cian)    
            canva1.create_text(200, 520, text="Colocar bloque de concreto", font=("Helvetica", 25), fill=cian) 
            canva1.create_text(200, 600, text="Colocar bloque de acero", font=("Helvetica", 25), fill=cian) 
            canva1.create_text(200, 720, text="Seleccionar/Recoger bloque", font=("Helvetica", 25), fill=cian) 
            
            canva1.create_text(1600, 440, text="Disparar bola de agua", font=("Helvetica", 25), fill=blood)    
            canva1.create_text(1600, 520, text="Disparar bola de fuego", font=("Helvetica", 25), fill=blood) 
            canva1.create_text(1600, 600, text="Disparar bomba", font=("Helvetica", 25), fill=blood) 
            canva1.create_text(1590, 720, text="Seleccionar/Pausar la partida", font=("Helvetica", 25), fill=blood)
        
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
                        global CancionAtacante
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
                        global CancionDefensor
                        CancionDefensor = archivo_seleccionado
                        print(CancionDefensor)
                
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
    
        
        def jugar():
            canva1.delete("all")
            window.destroy()
            stfu()
        canva1.create_image(375,416 , anchor=tk.NW, image=a)
        canva1.create_image(375,492 , anchor=tk.NW, image=a)
        canva1.create_image(375,565 , anchor=tk.NW, image=a)
        canva1.create_image(375,642 , anchor=tk.NW, image=a)
        canva1.create_image(375,727 , anchor=tk.NW, image=a)
        canva1.create_image(375,802 , anchor=tk.NW, image=a)
        
        btn_cargar = tk.Button(window , text="Elegir Canción", command=reproducir_mp3)
        
        playbtn = Button(canva1,width=Play.width(),height=Play.height(),image=Play,command=jugar,bg="black")
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


def obtener_duracion_mp3(ruta_archivo):
    try:
        mp3 = MP3(ruta_archivo)
        duracion = mp3.info.length  # Duración en segundos
        return duracion
    except Exception as e:
        print(f"Error al obtener la duración de la canción: {str(e)}")
        return None

def stfu ():
    
    # Inicializar Pygame
    pygame.init()
    
    global CancionDefensor
    
    # Colores
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    
    # Carga de imágenes
    tanque = pygame.image.load("Imágenes/Tanque_EagleF.png")
    woodenblock = pygame.image.load("Imágenes/woodenblock.png")
    ironblock = pygame.image.load("Imágenes/ironblock.png")
    stoneblock = pygame.image.load("Imágenes/stoneblock.png")
    waterbullet = pygame.image.load("Imágenes/bullet.png")
    firebullet = pygame.image.load("Imágenes/fire.png")
    bombullet = pygame.image.load("Imágenes/bomb.png")
    explosion_image = pygame.image.load("Imágenes/exp.png")
    background_image = pygame.image.load("fondo_part.png")
    shot_image = pygame.image.load("exp1.png")
    # Dimensiones de la ventana
    width, height = 800, 600
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Movimiento, disparo y creación de cuadros')
    
    # Tamaño del cuadro y de la bola
    square_size = 30
    ball_radius = 10  # Aumentar el tamaño de la bola
    
    # Posición inicial del cuadro y la bola
    square_x, square_y = width // 2, height // 2
    ball_x, ball_y = -10, -10  # Inicialmente la bola está fuera de la pantalla
    
    ball_speed = 3.5  # Reducir aún más la velocidad de las bolas
    global ball_direction
    ball_direction = None  # Dirección de la bola
    
    # Imágenes para los cuadros creados
    current_images = [woodenblock, ironblock, stoneblock]
    current_image_index = 0
    
    # Vidas correspondientes a cada tipo de bloque
    lives_for_blocks = [1, 3, 2]  # Se cambia el valor del stoneblock a 2
    
    # Lista para almacenar las posiciones de los cuadros creados junto con sus vidas
    created_squares = []
    
    # Diccionario para rastrear cuántos bloques de cada tipo se han creado
    created_block_counts = {
        woodenblock: 0,
        ironblock: 0,
        stoneblock: 0
    }
    
    # Variable para manejar el tipo de bala
    bullet_types = [waterbullet, firebullet, bombullet]
    current_bullet = 0
    
    # Variables para el movimiento
    moving_up = False
    moving_down = False
    moving_left = False
    moving_right = False
    uwu= False
    
    # Velocidad del tanque
    tank_speed = 1
    
    # Lista de tuplas para el seguimiento de colisiones de bombullet con ironblock
    bombullet_collisions = []
    
    # Límite de balas disponibles para cada tipo
    available_bullets = [5, 5, 5]  # Inicialmente, tienes 5 balas de cada tipo
    
    # Tiempo desde la última regeneración de balas
    time_since_last_regeneration = 0
    
    # Lista para rastrear los bloques destruidos junto con su tiempo de destrucción
    destroyed_squares = []
    
    pygame.mixer.init()
    atack = False

    # Estado de pausa
    paused = False

    # Botón de pausa - definir posición y tamaño
    pause_button_rect = pygame.Rect(width - 100, 10, 80, 30)
    pause_button_color = RED
    pause_button_text = 'Pause'

    current_time = time.time()  # Esto dará el tiempo actual en segundos desde la época (1 de enero de 1970).

    shot_animations = []  # Lista para almacenar las animaciones de disparo
    shot_image = pygame.image.load("exp1.png")
    # Función para dibujar el botón de pausa
    def draw_pause_button():
        pygame.draw.rect(window, pause_button_color, pause_button_rect)
        font = pygame.font.Font(None, 24)
        text = font.render(pause_button_text, True, WHITE)
        text_rect = text.get_rect(center=pause_button_rect.center)
        window.blit(text, text_rect)

    # Función para alternar el estado de pausa
    def toggle_pause():
        global paused, pause_button_text
        paused = not paused
        pause_button_text = 'Resume' if paused else 'Pause'

    # Función para dibujar los contadores de balas
    def draw_bullet_counters():
        font = pygame.font.Font(None, 24)
        water_bullet_pos = (10, height - 70)
        fire_bullet_pos = (10, height - 45)
        bomb_bullet_pos = (10, height - 20)
        pygame.draw.rect(window, WHITE, (water_bullet_pos[0], water_bullet_pos[1], 150, 60))
        water_bullet_text = font.render(f'Water Bullets: {available_bullets[0]}', True, RED)
        fire_bullet_text = font.render(f'Fire Bullets: {available_bullets[1]}', True, RED)
        bomb_bullet_text = font.render(f'Bomb Bullets: {available_bullets[2]}', True, RED)

        window.blit(water_bullet_text, water_bullet_pos)
        window.blit(fire_bullet_text, fire_bullet_pos)
        window.blit(bomb_bullet_text, bomb_bullet_pos)

    # Función para dibujar los contadores de bloques
    def draw_block_counters():
        font = pygame.font.Font(None, 24)
        # Definir las posiciones para los contadores
        wooden_block_pos = (width - 150, height - 70)
        iron_block_pos = (width - 150, height - 45)
        stone_block_pos = (width - 150, height - 20)

        # Dibujar el fondo para los contadores
        pygame.draw.rect(window, WHITE, (wooden_block_pos[0], wooden_block_pos[1], 150, 60))

        # Mostrar el texto para cada contador
        wooden_block_text = font.render(f'Wood: {5 - created_block_counts[woodenblock]}', True, RED)
        iron_block_text = font.render(f'Iron: {5 - created_block_counts[ironblock]}', True, RED)
        stone_block_text = font.render(f'Stone: {5 - created_block_counts[stoneblock]}', True, RED)

        window.blit(wooden_block_text, wooden_block_pos)
        window.blit(iron_block_text, iron_block_pos)
        window.blit(stone_block_text, stone_block_pos)

    def handle_explosions(destroyed_squares, current_time):
        for destroyed_square in destroyed_squares:
            if destroyed_square.get('animate', False):
                time_since_destruction = current_time - destroyed_square['time']
                if time_since_destruction <= 500:  # La duración de la animación de explosión es de 500 ms
                    window.blit(explosion_image, destroyed_square['rect'].topleft)
                else:
                    destroyed_square['animate'] = False  # Termina la animación después de 500 ms

    def check_space_occupied(x, y, squares):
        for square in squares:
            if square['rect'].colliderect(pygame.Rect(x, y, square_size, square_size)):
                return True
        return False


    def cambiar_cancion_si_necesario():
        global cambios  # Declarar 'cambios' como una variable global dentro de la función
        if atack and cambios == 0:
            cambios = cambios + 1
            pygame.mixer.music.load(os.path.join("Canciones", CancionAtacante))
            pygame.mixer.music.play()


    def musica():
    # Verifica si la música no se está reproduciendo actualmente
        if not pygame.mixer.music.get_busy():
            # Reproduce la canción
            pygame.mixer.music.load(os.path.join(carpeta, CancionDefensor))
            pygame.mixer.music.play()

    def check_collisions(created_squares, ball_x, ball_y, ball_radius, current_bullet, bombullet_collisions):
        global ball_direction

        current_time = pygame.time.get_ticks()  # Obtén el tiempo actual

        ball_rect = pygame.Rect(ball_x - ball_radius, ball_y - ball_radius, 2 * ball_radius, 2 * ball_radius)
        ball_collided = False
        if ball_direction:
            for square_data in created_squares[:]:
                square = square_data['rect']
                if ball_x > 0 and ball_y > 0:
                    ball_rect = pygame.Rect(ball_x - ball_radius, ball_y - ball_radius, 2 * ball_radius,
                                            2 * ball_radius)
                    if ball_rect.colliderect(square):
                        if not square_data.get('hit', False):
                            if current_bullet == 0:
                                if square_data['image'] == ironblock:
                                    square_data['lives'] -= 2
                                elif square_data['image'] == woodenblock:
                                    square_data['lives'] -= 3
                                elif square_data['image'] == stoneblock:
                                    square_data['lives'] -= 0.8
                            elif current_bullet == 1:
                                if square_data['image'] == ironblock:
                                    square_data['lives'] -= 3  # Firebullet
                                elif square_data['image'] == woodenblock:
                                    square_data['lives'] -= 3
                                else:
                                    square_data['lives'] -= 1.5
                            elif current_bullet == 2:
                                if square_data['image'] == ironblock:
                                    square_data['lives'] -= 3
                                elif square_data['image'] == woodenblock:
                                    square_data['lives'] -= 3
                                else:
                                    square_data['lives'] -= 3

                                if square_data['image'] != ironblock:
                                    square_data['lives'] = 0
                                else:
                                    ironblock_collision = next(
                                        (collision for collision in bombullet_collisions if
                                         collision[0] == square_data), None)
                                    if ironblock_collision is not None:
                                        if ironblock_collision[1] >= 1:
                                            square_data['lives'] = 0
                                        else:
                                            ironblock_collision[1] += 1
                                    else:
                                        bombullet_collisions.append((square_data, 1))
                            square_data['hit'] = True
                            ball_collided = True
                            if square_data['lives'] <= 0:
                                # Registra el bloque destruido junto con el tiempo actual
                                destroyed_squares.append({'rect': square_data['rect'], 'time': current_time})
                                created_squares.remove(square_data)
                                destroyed_squares.append(
                                    {'rect': square_data['rect'], 'time': current_time, 'animate': True})

                            ball_direction = None

        if not ball_collided:
            for square_data in created_squares:
                square_data.pop('hit', None)
                
    carpeta = "Canciones"
    tiempo_inicial = time.time()
    running = True
    while running:
        window.blit(background_image, (0, 0))
        draw_pause_button()
        draw_bullet_counters()
        draw_block_counters()
        handle_explosions(destroyed_squares, current_time)
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            

            segundos_a_contar = obtener_duracion_mp3("Canciones/"+CancionDefensor) 
            final = obtener_duracion_mp3("Canciones/"+CancionDefensor) + obtener_duracion_mp3("Canciones/"+CancionAtacante)
            
            
            # Función que se llamará al finalizar el contador
            def otra_funcion():
                print("El contador ha finalizado.")
                # Realiza acciones adicionales aquí
            tiempo_actual = time.time()
            tiempo_transcurrido = tiempo_actual - tiempo_inicial
            
            if tiempo_transcurrido >= final:
                pygame.quit()
                ventana_principal()
            
            if tiempo_transcurrido >= segundos_a_contar and tiempo_transcurrido < final :
                atack = True
                cambiar_cancion_si_necesario()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        moving_up = True
                    elif event.key == pygame.K_s:
                        moving_down = True
                    elif event.key == pygame.K_a:
                        moving_left = True
                    elif event.key == pygame.K_d:
                        moving_right = True
        
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w:
                        moving_up = False
                    elif event.key == pygame.K_s:
                        moving_down = False
                    elif event.key == pygame.K_a:
                        moving_left = False
                    elif event.key == pygame.K_d:
                        moving_right = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_k and ball_direction is None:
                        if available_bullets[current_bullet] > 0:
                            ball_direction = "left"
                            ball_x, ball_y = square_x, square_y + square_size // 2
                            # Inicia la animación del disparo
                            shot_animations.append({
                                'position': (square_x, square_y),
                                'start_time': current_time
                            })
                            available_bullets[current_bullet] -= 1
            
            
            if tiempo_transcurrido <= segundos_a_contar:
                musica()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        block_type = current_images[current_image_index]
                        # Verifica si aún hay bloques disponibles antes de crear uno
                        if created_block_counts[block_type] < 5:
                            created_squares.append({
                                'rect': pygame.Rect(mouse_x, mouse_y, square_size, square_size),
                                'lives': lives_for_blocks[current_image_index],
                                'image': block_type
                            })
                            created_block_counts[block_type] += 1


                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        current_image_index = (current_image_index + 1) % len(current_images)
                    elif event.key == pygame.K_p:
                        current_bullet = (current_bullet + 1) % len(bullet_types)
                current_time = pygame.time.get_ticks()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        mouse_x, mouse_y = event.pos
                        if pause_button_rect.collidepoint(mouse_x, mouse_y):
                            toggle_pause()

        current_time = pygame.time.get_ticks()
        if not paused:
            for destroyed_square in destroyed_squares[:]:
                if current_time - destroyed_square['time'] >= 25000:  # 5000 ms = 5 segundos
                    created_squares.append({
                        'rect': destroyed_square['rect'],
                        'lives': lives_for_blocks[current_image_index],
                        'image': current_images[current_image_index]
                    })
                    destroyed_squares.remove(destroyed_square)

            if moving_up and square_y > 0:
                square_y -= tank_speed
            if moving_down and square_y < height - square_size:
                square_y += tank_speed
            if moving_left and square_x > 0:
                square_x -= tank_speed
            if moving_right and square_x < width - square_size:
                square_x += tank_speed

            if ball_direction == "left":
                ball_x -= ball_speed

            if ball_x < 0:
                ball_direction = None
                ball_x, ball_y = -10, -10

            window.blit(tanque, (square_x, square_y))

            for square_data in created_squares:
                square = square_data['rect']
                image = square_data['image']
                window.blit(image, square.topleft)

            check_collisions(created_squares, ball_x, ball_y, ball_radius, current_bullet, bombullet_collisions)

            if ball_direction:
                window.blit(bullet_types[current_bullet], (int(ball_x) - ball_radius, int(ball_y) - ball_radius))

            current_time = pygame.time.get_ticks()
            if current_time - time_since_last_regeneration >= 30000:  # 30 segundos
                available_bullets = [5, 5, 5]
                time_since_last_regeneration = current_time


        else:
            font = pygame.font.Font(None, 74)
            text = font.render('PAUSA', True, RED)
            text_rect = text.get_rect(center=(width // 2, height // 2))
            window.blit(text, text_rect)

        for shot in shot_animations[:]:
            if current_time - shot['start_time'] > 200:  # La duración de la animación de disparo
                shot_animations.remove(shot)
            else:
                window.blit(shot_image, shot['position'])

        pygame.display.update()

    pygame.quit()
    sys.exit()