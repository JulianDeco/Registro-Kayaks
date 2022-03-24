from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import tkinter as tk
import functools
import operator
from menu_kayak import registro_kayaks
from menu_perchas import perchas_kayak
from menu_registro import menu_registro

# Agregar carteles que señalen si hay un error






ventana_principal = Tk()
ventana_principal.title("Prueba X")
ventana_principal.geometry("300x380")



Label(ventana_principal,text="Acceso al sistema", bg="#EB4B28", fg="white", width="300", height="3", font=("Calibri", 15)).pack()
Label(ventana_principal,text="").pack()

Button(ventana_principal,text="Ver clientes", height="3", width="30", command=menu_registro).pack()
Label(ventana_principal,text="").pack()

Button(ventana_principal,text="Ver kayaks", height="3", width="30", command=registro_kayaks).pack()
Label(ventana_principal,text="").pack()
Button(ventana_principal,text="Ver perchas", height="3", width="30", command=perchas_kayak).pack()



ventana_principal.mainloop()