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
from mutagen.mp3 import MPEGInfo
from mutagen import File
import os

import Juego

from PIL import Image, ImageTk
import pygame

from Utils import user1 , user2 

MAX_DURACION = 5 * 60  # Duración máxima en segundos (5 minutos)
def ppp():
    Juego.ventana_principal()

def asignar_user (userName):
    global user1
    global user2
    if user1 == "":
        user1=userName
    else:
        user2=userName
        
def cargar_cancion():
    ruta_archivo = filedialog.askopenfilename()
    if ruta_archivo:
        duracion = obtener_duracion_mp3(ruta_archivo)
        if duracion is not None :
            if duracion <= MAX_DURACION:
                guardar_cancion(ruta_archivo, 'Canciones')
            else:
                cortada = cortar_cancion(ruta_archivo)
                guardar_cancion(cortada, 'Canciones')
        elif duracion is not None:
            messagebox.showerror("ERROR", "La canción debe de durar menos de cinco minutos")

def obtener_duracion_mp3(ruta_archivo):
    try:
        mp3 = MP3(ruta_archivo)
        duracion = mp3.info.length  # Duración en segundos
        return duracion
    except Exception as e:
        print(f"Error al obtener la duración de la canción: {str(e)}")
        return None

def cortar_cancion(input_file):
    # Abre el archivo de entrada MP3
    audio = MP3(input_file)

    # Obtiene la duración en segundos de la canción
    original_duration = audio.info.length

    # Define la duración objetivo en segundos (3 minutos y 30 segundos)
    target_duration = 3 * 60 + 30

    # Comprueba si la canción necesita ser cortada
    if original_duration > target_duration:
        # Obtén la ruta completa del archivo de salida
        output_file = os.path.join(os.path.dirname(input_file), "cancion_cortada.mp3")
        os.system(f'ffmpeg -i "{input_file}" -t {target_duration} -acodec copy "{output_file}"')
        return output_file
    else:
        return input_file
    
def guardar_cancion(ruta_archivo, destino):
    try:
        # Copiar el archivo original a la ubicación de destino
        shutil.copy(ruta_archivo, destino)
        print("Canción guardada exitosamente.")
    except Exception as e:
        print(f"Error al guardar la canción: {str(e)}")

        
def mostrar_error(users):
    if users == 2:
        print (user1)
        print (user2)
        window.destroy()
        Juego.ventana_principal()

    else:
        pass
    
def login():
    global user1
    fonde = Image.open("Imágenes/5122533.png") 
    imagen = ImageTk.PhotoImage(fonde)
    def login_database():
        global users
        global user1        
        conn = sqlite3.connect("2.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM test WHERE email=? AND password=?", (e1.get(), e2.get()))
        asignar_user(e1.get())
        row = cur.fetchall()
        conn.close()
        print(row)
        if row != []:
            user_name = row[0][1]
            l3.config(text="Usuario encontrado con nombre: " + user_name)
            login_window.destroy()  # Destroy the login_window when done
            users +=1
            mostrar_error(users)

        else:
            l3.config(text="Usuario no encontrado")

    login_window = Tk()
    login_window.geometry("500x200")
    login_window.resizable(False, False) #Se establece que la ventana no se puede agrandar
    
    

   

    l1 = Label(login_window, text="Email", font="times 20")
    l1.grid(row=1, column=1)
    l2 = Label(login_window, text="Contraseña", font="times 20")
    l2.grid(row=2, column=1)
    l3 = Label(login_window, font="times 20")
    l3.grid(row=5, column=2)

    email_text = StringVar()
    e1 = Entry(login_window, textvariable=email_text)
    e1.grid(row=1, column=2)
    password_text = StringVar()
    e2 = Entry(login_window, textvariable=password_text)
    e2.grid(row=2, column=2)

    b1 = Button(login_window, text="Iniciar sesión", width=20, command=login_database)
    b1.grid(row=4, column=2)

    login_window.mainloop()

def signup():
    def signup_database():
        global users
        conn = sqlite3.connect("2.db")
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS test(id INTEGER PRIMARY KEY, name text, email text, password text, birth text)")
        cur.execute("INSERT INTO test VALUES(NULL,?,?,?,?)", (e1.get(), e2.get(), e3.get(), e4.get()))
        asignar_user(e1.get())
        l4 = Label(signup_window, text="Cuenta creada", font="times 15")
        l4.grid(row=6, column=2)
        conn.commit()
        conn.close()
        mostrar_error(users)
        users +=1
        mostrar_error(users) 

        

    signup_window = Tk()
    signup_window.geometry("400x250")
    
    
    l1 = Label(signup_window, text="Nombre de usuario", font="times 20")
    l1.grid(row=1, column=1)
    l2 = Label(signup_window, text="Email", font="times 20")
    l2.grid(row=2, column=1)
    l3 = Label(signup_window, text="Contraseña", font="times 20")
    l3.grid(row=3, column=1)
    l4 = Label(signup_window, text="Fecha de nacimiento", font="times 20")
    l4.grid(row=4, column=1)

    name_text = StringVar()
    e1 = Entry(signup_window, textvariable=name_text)
    e1.grid(row=1, column=2)
    email_text = StringVar()
    e2 = Entry(signup_window, textvariable=email_text)
    e2.grid(row=2, column=2)
    password_text = StringVar()
    e3 = Entry(signup_window, textvariable=password_text)
    e3.grid(row=3, column=2)
    birth_text = StringVar()
    e4 = Entry(signup_window, textvariable=birth_text)
    e4.grid(row=4, column=2)

    b1 = Button(signup_window, text="Registrarse", width=20, command=signup_database)
    b1.grid(row=5, column=2)
 
    signup_window.mainloop()
    
def exitt():
    pygame.mixer.music.stop()
    window.destroy()
    
window = Tk()
window.geometry("750x750")
window.resizable(False, False) #Se establece que la ventana no se puede agrandar

imagen = Image.open("Imágenes/5122533 (1).png")  
imagen_tk = ImageTk.PhotoImage(imagen)

INS=PhotoImage(file="Imágenes/BOTON INISES.png")
REG=PhotoImage(file="Imágenes/BOTON REG.png") 
MUS=PhotoImage(file="Imágenes/BOTON MUS.png") 
EXIT=PhotoImage(file="Imágenes/BOTON SALIR.png")

# Crear una etiqueta para mostrar la imagen
etiqueta = tk.Label(window, image=imagen_tk)
etiqueta.place(x=0, y=0)


b1 = Button(window, width=20, command=login, image= INS)
b1.config(width=INS.width(), height=INS.height())  # Configurar el tamaño del botón
b1.place(x=175 , y=630)

b2 = Button(window, width=REG.width(),height=REG.height(),image=REG, command=signup)
b2.place(x=175 , y=500)

b3 = Button(window, width=EXIT.width(),height=EXIT.height(),image=EXIT, command=exitt)
b3.place(x=0 , y=0)


btn_cargar = tk.Button(window, width=MUS.width(),height=MUS.height(), command=cargar_cancion, image=MUS)
btn_cargar.place(x=620, y=10)

window.mainloop()

