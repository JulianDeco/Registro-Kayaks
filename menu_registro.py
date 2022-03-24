from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import tkinter as tk
import functools
import operator

def menu_registro():
    def mostrar_datos():
        guardar = Tabla.get_children() #obtener elementos de la tabla
        for element in guardar:
            Tabla.delete(element)
        conexion=sqlite3.connect("prueba.db")
        cursor=conexion.cursor()
        cursor.execute('SELECT * FROM Clientes ORDER BY apellidos DESC')
        i=cursor.fetchall()
        for row in i:
            Tabla.insert('',0,text=row, values=row)
        conexion.commit()
        conexion.close()

    def buscar_datos():
            guardar = Tabla.get_children() #obtener elementos de la tabla
            for element in guardar:
                Tabla.delete(element)
            conexion=sqlite3.connect("prueba.db")
            cursor=conexion.cursor()
            a = search.get()
            print(a)
            cursor.execute("SELECT * FROM CLIENTES WHERE apellidos=('" + search.get()+ "')")
            i=cursor.fetchall()
            for row in i:
                Tabla.insert('',0,text='', values=row)
            conexion.commit()
            conexion.close()

    def guardar_datos():
                try:
                    conexion=sqlite3.connect("prueba.db")
                    cursor=conexion.cursor()
                    print(nombres.get())
                    print(apellidos.get())
                    cursor.execute("INSERT INTO Clientes VALUES(NULL,'" + apellidos.get() +
                        "','"+ nombres.get() + "')")
                                            
                    conexion.commit()
                    conexion.close()
                                    
                    mostrar_datos()
                except:
                    messagebox.showwarning("Aviso","Este usuario ya existe o\ndejó campos vacíos.")

    def edit_products():
                pass

    def salirAplicacion():
            
            valor=messagebox.askquestion("Salir", "¿Deseas salir de la aplicación?")

            if valor=='yes':
                ventana.destroy()
            


    def borrar_datos():
                c=messagebox.askquestion("Aviso","¿Desea borrar lo seleccionado?")
                if c=='yes':
                        selected_item = Tabla.selection()[0] ## get selected item
                        
                        print(selected_item)
                        
                        
                        # Perchas = Tabla.item(Tabla.selection())
                        Conexion=sqlite3.connect('prueba.db')
                        cursor=Conexion.cursor()
                        cursor.execute("SELECT codigo_kayak FROM Kayak WHERE codigo__cliente = ?", (Tabla.set(selected_item, '#1'),))
                        a=cursor.fetchall()
                        cursor.execute("DELETE FROM Clientes WHERE codigo_cliente = ?", (Tabla.set(selected_item, '#1'),))
                        Conexion.commit()
                        cursor.execute("DELETE FROM Kayak WHERE codigo__cliente = ?", (Tabla.set(selected_item, '#1'),))
                        Conexion.commit()
                        b=functools.reduce(operator.add, (a)) #Utilizar esto en registro de clientes
                        print(b)
                        print(a)
                        j=functools.reduce(operator.add, (b))
                        g=str(j)
                        print(g)
                        if len(a)>1:
                            n=1
                            output=[a[i:i + n] for i in range(0, len(a), n)]
                            
                                        
                            h=functools.reduce(operator.add, (output))
                                        
                            j=functools.reduce(operator.add, (h))
                            f=str(j)
                            print(f)
                            print(f[2])    
                            def total_elements(list):
                                    count = 0
                                    for elementos in list:
                                                count += 1
                                    return count
                                        # no funciona con más de un kayak
                            wo=(total_elements(a))
                            str1 = ' '.join(str(e) for e in j)
                            e=range(wo)
                            print(e)
                            for number in e:
                                c=a[number]
                                print(c)
                                b=functools.reduce(operator.add, (c)) #Utilizar esto en registro de clientes
                                k=str(b)
                                cursor.execute("DELETE FROM Percha WHERE codigo__kayak = ?",(k),)
                                Conexion.commit()
                        else:
                            cursor.execute("DELETE FROM Percha WHERE codigo__kayak = ?",(g),)
                            Conexion.commit()
                        
                        Tabla.delete(selected_item)
                mostrar_datos()#se utiliza para actualizar la lista
                

    ventana= tk.Toplevel()
            
            
    ventana.title('Guarderia')
    ventana.config(bg="light blue")
        
        
        
            #frame contenedor
    miframe=LabelFrame(ventana, height=20, padx=100)
    miframe.grid(row = 0,column=0, columnspan = 3 , pady=20, padx=400)

    
    apellidos=StringVar()
    nombres=StringVar()
        
            #Label y entry
    Label(miframe, text="Apellido: ").grid(row=1, column=0, sticky=W)
    apellido = Entry(miframe, textvariable=apellidos)
    apellido.grid(row=1,column=1)

    Label(miframe, text="Nombre: ").grid(row=2, column=0, sticky=W)
    nombre = Entry(miframe, textvariable=nombres)
    nombre.grid(row=2,column=1)





    # botón
    Button(miframe, text="Guardar", command=guardar_datos).grid(row=7, sticky=W+E, columnspan=2, pady=10, padx=20)

    # frame 2

    miframe2=LabelFrame(ventana, height=20, padx=100)
    miframe2.grid(row = 8,column=0, columnspan = 4 , pady=20, padx=300)


    # boton buscar
    search=StringVar()
    Button(miframe2, text="Buscar", command=buscar_datos).grid(row=9, sticky=W+E, columnspan=2, pady=10, padx=15)
    busqueda=Entry(miframe2, textvariable=search)
    busqueda.grid(row=9, column=2)
    Button(miframe2, text="Actualizar", command=mostrar_datos).grid(row=10, sticky=W+E, columnspan=3, pady=10, padx=15)

    # tabla

    Tabla=ttk.Treeview(ventana,height=10, columns=('#1','#2','#3'))
    Tabla.grid(row=10, columnspan=5)
    Tabla.heading('#0' , text="", anchor="w")
    Tabla.heading('#1', text="ID", anchor=CENTER)
    Tabla.heading('#2', text="Apellido", anchor=CENTER)
    Tabla.heading('#3', text="Nombre", anchor=CENTER)

    Tabla.column("#0",stretch=False, width=1)
    Tabla.column("#1",stretch=False, width=1)

    #scroll
    scrollvertical=Scrollbar(ventana, command=Tabla.yview)
    scrollvertical.grid(sticky="nsnew", row=10, column=4)


    Tabla.config(yscrollcommand=scrollvertical.set)

    mostrar_datos()

    #botones inferiores

    Button(ventana, text="Salir", command=salirAplicacion).grid(row=12, sticky=W+E, column=0, pady=10, padx=15)
    Button(ventana, text="Borrar", command=borrar_datos).grid(row=12, sticky=W+E, column=1, pady=10, padx=15)
    Button(ventana, text="Editar", command=None).grid(row=12, sticky=W+E, column=2, pady=10, padx=15)

    ventana.mainloop()