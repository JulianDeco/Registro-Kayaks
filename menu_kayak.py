"""
QUEDA POR RESOLVER:
    -Nombre con llaves
    -Registro kayak persona c/ 2 dos nombres o 2 apellidos // RESUELTO
    -Busqueda de kayak p/ persona c/ 2 nombres o 2 apellidos //RESUELTO
"""



from tkinter import *
from tkinter import messagebox
from tkinter import ttk 
import tkinter as tk
import sqlite3
import functools
import operator

def registro_kayaks():
    def mostrar_datos_kayak(): #MUESTRA LOS DATOS AL INICIO
        guardar2 = Tabla_kayak.get_children() #obtener elementos de la tabla
        for element in guardar2:
            Tabla_kayak.delete(element)
        conexion=sqlite3.connect("prueba.db")
        cursor=conexion.cursor()
        cursor.execute('SELECT * FROM Kayak')
        i=cursor.fetchall()
        print(i)
        cursor.execute('SELECT codigo__cliente FROM Kayak')
        d=cursor.fetchall()
        n=1
        output=[d[i:i + n] for i in range(0, len(d), n)]
        
                    
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
        wo=(total_elements(d))
        str1 = ' '.join(str(e) for e in j)
        e=range(wo)
        print(e)
        for number in e:
            a=d[number]
            b=functools.reduce(operator.add, (a)) #Utilizar esto en registro de clientes
            k=str(b)
            print(k)
            cursor.execute("SELECT apellidos, nombres FROM Clientes WHERE codigo_cliente=('" + k +"')")
            c=cursor.fetchall()
            Tabla_kayak.insert('',tk.END,text=c, values=i[number])
            
        conexion.commit()

    def borrar_datos2(): #BORRA DATOS
            c=messagebox.askquestion("Aviso","¿Desea borrar lo seleccionado?")
            if c=='yes':
                    selected_item = Tabla_kayak.selection()[0] ## get selected item
                    
                    print(selected_item)
                    
                    
                    # Perchas = Tabla.item(Tabla.selection())
                    Conexion=sqlite3.connect('prueba.db')
                    cursor=Conexion.cursor()
                    cursor.execute("DELETE FROM Percha WHERE codigo__kayak = ?", (Tabla_kayak.set(selected_item, '#1'),))
                    cursor.execute("DELETE FROM Kayak WHERE codigo_kayak = ?", (Tabla_kayak.set(selected_item, '#1'),))
                    i=cursor.fetchall()
                    print(i)
                    Conexion.commit()
                    Tabla_kayak.delete(selected_item)
                    # messagebox.showinfo('Producto {} eliminado satisfactoriamente'.format(perchas))
            mostrar_datos_kayak()#se utiliza para actualizar la lista
    
    def buscar_kayak(): #BUSCA KAYAK
        
            a =(lista_desplegable2.get())
            value = a.split()
            print(value)
            guardar2 = Tabla_kayak.get_children() #obtener elementos de la tabla
            for element in guardar2:
                Tabla_kayak.delete(element)
            conexion=sqlite3.connect("prueba.db")
            cursor=conexion.cursor()
            if len(value)<3: # SI UN NOMBRE TIENE 1 NOMBRE Y 1 APELLIDO UTILIZA ESTE CAMINO    
                cursor.execute("SELECT codigo_cliente FROM Clientes WHERE nombres =('" + value[0]+ "') AND apellidos =('" + value[1]+ "')") # WHERE type = "table" AND name = "employees"')
                a=cursor.fetchone()
                print(a)
                b=functools.reduce(operator.add, (a)) #Utilizar esto en registro de clientes
                c=str(b)
                print(c)
                cursor.execute("SELECT * FROM Kayak WHERE codigo__cliente=('" +c+ "')")
                i=cursor.fetchall()
                print(i)
                for row in i:
                    Tabla_kayak.insert('',tk.END,text=value, values=row)
                conexion.commit()
            
            else: # SI UN NOMBRE TIENE MÁS DE 1 NOMBRE O 1 APELLIDO UTILIZA ESTE CAMINO
                    characters="{","}"
                    for x in range(len(characters)):
                        a = a.replace(characters[x],"")    
                    print(a)
                    c=a.split(" ",2)
                    print(c)
                    x=c[0]+" "+c[1]
                    print(x)
                    cursor.execute("SELECT codigo_cliente FROM Clientes WHERE apellidos =('" +c[2]+ "') AND nombres =('" + x+ "')")
                    a=cursor.fetchone()
                    print(a)
                    b=functools.reduce(operator.add, (a)) #Utilizar esto en registro de clientes
                    g=str(b)
                    print(g)
                    cursor.execute("SELECT * FROM Kayak WHERE codigo__cliente=('" +g+ "')")
                    w=cursor.fetchall()
                    print(w)
                    for row in w:
                        Tabla_kayak.insert('',tk.END,text=x+" "+c[2], values=row)
                    conexion.commit()
                    
               
    def poner_clientes(): #PONE CLIENTES EN LA CAJA
        conexion=sqlite3.connect("prueba.db")
        cursor=conexion.cursor()
        cursor.execute('SELECT nombres, apellidos FROM Clientes')
        i=cursor.fetchall()
        data = []
        for rows in i:
            data.append(rows)
        return data

    def mostrar_datos_kayak2(): #2DA CAJA BUSCADOR
            a =(lista_desplegable.get())
            print(a)
            value = a.split()
            print(value)
            conexion=sqlite3.connect("prueba.db")
            cursor=conexion.cursor()
            if len(value)<3: # SI UN NOMBRE TIENE 1 NOMBRE Y 1 APELLIDO UTILIZA ESTE CAMINO
                cursor.execute("SELECT codigo_cliente FROM Clientes WHERE nombres =('" + value[0]+ "') AND apellidos =('" + value[1]+ "')") # WHERE type = "table" AND name = "employees"')
                a=cursor.fetchone()
                print(a)
                b=functools.reduce(operator.add, (a)) #Utilizar esto en registro de clientes
                c=str(b)
                print(c)
                cursor.execute("INSERT INTO Kayak VALUES(NULL,'" + c + "','"+ modelos.get() + "','"+ colors.get() + "')") #"INSERT INTO Clientes VALUES(NULL,'" + apellidos.get() + "','"+ nombres.get() + "')")
                conexion.commit()
                
                print(c)
                conexion2=sqlite3.connect("prueba.db")
                cursor2=conexion2.cursor()
                cursor2.execute("SELECT codigo_kayak FROM Kayak WHERE codigo__cliente=('" + c + "') AND tipo =('" + modelos.get()+ "')AND color =('" + colors.get()+ "')")
                o=cursor2.fetchone()
                conexion2.commit()
                print(o)
                q=functools.reduce(operator.add, (o)) #Utilizar esto en registro de clientes
                number = str(q)
                print(number)
                print(perchas.get())
                cursor2.execute("INSERT INTO Percha VALUES('" + perchas.get() + "','" + number + "')")
                conexion2.commit()
            else:
                characters="{","}"
                for x in range(len(characters)):
                    a = a.replace(characters[x],"")    
                print(a)
                c=a.split(" ",2)
                print(c)
                x=c[0]+" "+c[1]
                print(x)
                cursor.execute("SELECT codigo_cliente FROM Clientes WHERE apellidos =('" +c[2]+ "') AND nombres =('" + x+ "')")
                a=cursor.fetchone()
                print(a)
                b=functools.reduce(operator.add, (a)) #Utilizar esto en registro de clientes
                c=str(b)
                print(c)
                cursor.execute("INSERT INTO Kayak VALUES(NULL,'" + c + "','"+ modelos.get() + "','"+ colors.get() + "')") #"INSERT INTO Clientes VALUES(NULL,'" + apellidos.get() + "','"+ nombres.get() + "')")
                conexion.commit()
                
                print(c)
                conexion2=sqlite3.connect("prueba.db")
                cursor2=conexion2.cursor()
                cursor2.execute("SELECT codigo_kayak FROM Kayak WHERE codigo__cliente=('" + c + "') AND tipo =('" + modelos.get()+ "')AND color =('" + colors.get()+ "')")
                o=cursor2.fetchone()
                conexion2.commit()
                print(o)
                q=functools.reduce(operator.add, (o)) #Utilizar esto en registro de clientes
                number = str(q)
                print(number)
                print(perchas.get())
                cursor2.execute("INSERT INTO Percha VALUES('" + perchas.get() + "','" + number + "')")
                conexion2.commit()    
            
            mostrar_datos_kayak()

    def salir_kayak(): #SALIR APLICACIÓN
        valor=messagebox.askquestion("Salir", "¿Deseas salir de la aplicación?")

        if valor=='yes':
            ventana2.destroy()

    #VENTANA--------------------------------------------------------------------

    ventana2 = tk.Toplevel()
    ventana2.title('Prueba de kayak con lista')
    ventana2['bg']='#fb0'

    frame=LabelFrame(ventana2,height=20, padx=200)
    frame.grid(row = 0,column=0, columnspan = 3 , pady=20, padx=20)

    #VARIABLES
    modelos=StringVar()
    colors=StringVar()
    perchas=StringVar()
    #FIN VARIABLES
    
    #LABEL y ENTRY

    Label(frame, text="Modelo: ").grid(row=1, column=0, sticky=W)
    modelo = Entry(frame, textvariable=modelos)
    modelo.grid(row=1,column=1)

    Label(frame, text="Color: ").grid(row=2, column=0, sticky=W)
    color = Entry(frame, textvariable=colors)
    color.grid(row=2,column=1)


    Label(frame, text="Cliente: ").grid(row=3, column=0, sticky=W)
    #COMBOBOX
    lista_desplegable=ttk.Combobox(frame, state="readonly")
    lista_desplegable.grid(row=3, column=1)
    lista_desplegable["values"] = poner_clientes()
    #LABEL Y ENTRY
    Label(frame, text="Percha: ").grid(row=4, column=0, sticky=W)
    percha = Entry(frame, textvariable=perchas)
    percha.grid(row=4,column=1)

    #BOTON
    Button(frame, text="Guardar", command=mostrar_datos_kayak2).grid(row=5, columnspan=2, sticky=W+E, padx=15, pady=20)

    #TABLA

    Tabla_kayak=ttk.Treeview(ventana2,height=10, columns=('#1','#2','#3','#4'))
    Tabla_kayak.grid(row=12, columnspan=5)
    Tabla_kayak.heading('#0' , text="Cliente", anchor="w")
    Tabla_kayak.heading('#1' , text="Cliente", anchor=CENTER)
    Tabla_kayak.heading('#2', text="Codigo_cliente", anchor=CENTER)
    Tabla_kayak.heading('#3', text="Modelo", anchor=CENTER)
    Tabla_kayak.heading('#4', text="Color", anchor=CENTER)
    Tabla_kayak.column('#1',stretch=False, width=1)

    scrollvertical=Scrollbar(ventana2, command=Tabla_kayak.yview)
    scrollvertical.grid(sticky="nsnew", row=12, column=5)


    Tabla_kayak.config(yscrollcommand=scrollvertical.set)
    search=StringVar()

    #BOTON
    Button(frame, text="Buscar", command=buscar_kayak).grid(row=9, column=0, sticky=W+E, pady=10, padx=15)
    lista_desplegable2=ttk.Combobox(frame, state="readonly")
    lista_desplegable2.grid(row=9, column=1)
    lista_desplegable2["values"] = poner_clientes()



    Button(frame, text="Eliminar", command=borrar_datos2).grid(row=11, sticky=W+E, column=0, pady=10, padx=10)
    Button(frame, text="Salir", command=salir_kayak).grid(row=11, sticky=W+E, column=1, pady=10, padx=10)
    Button(frame, text="Actualizar", command=mostrar_datos_kayak).grid(row=11, sticky=W+E, column=2, pady=10, padx=10)


    mostrar_datos_kayak()



    ventana2.mainloop()

