from tkinter import *
from tkinter import messagebox
from tkinter import ttk 
import tkinter as tk
import sqlite3
import functools
import operator

"""
-Nombre con llave
"""

#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------

def perchas_kayak():   

#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------


    def poner_datos(): #Carga los datos al inicio
        guardar2 = Tabla_kayak.get_children() #obtener elementos de la tabla
        for element in guardar2:
            Tabla_kayak.delete(element)
        conexion=sqlite3.connect("prueba.db")
        cursor=conexion.cursor()
        cursor.execute("SELECT numero FROM Percha ORDER BY codigo__kayak ASC ")
        i=cursor.fetchall()
        cursor.execute("SELECT tipo,color FROM Kayak")
        o=cursor.fetchall()
        cursor.execute("SELECT codigo__cliente FROM kayak")
        d=cursor.fetchall()
        cursor.execute("SELECT nombres,apellidos FROM Clientes")
        g=cursor.fetchall()
        print(i)
        print(o)
        print(g)
        a=len(o)
        x=range(a)
        print(x)
        for numer in x:
            a=d[numer]
            b=functools.reduce(operator.add, (a)) #Utilizar esto en registro de clientes
            k=str(b)
            cursor.execute("SELECT apellidos, nombres FROM Clientes WHERE codigo_cliente=('" + k +"')")
            c=cursor.fetchall()
            Tabla_kayak.insert("",tk.END,text=c,values=(i[numer]+o[numer]))
        #for row in i:
            #for raw in o:
                #Tabla_kayak.insert("",tk.END, text=row, values=raw)
                
    def actualizar_datos(): # ACTUALIZACIÓN DE DATOS
            guardar2 = Tabla_kayak.get_children() #obtener elementos de la tabla
            for element in guardar2:
                Tabla_kayak.delete(element)
            conexion=sqlite3.connect("prueba.db")
            cursor=conexion.cursor()
            cursor.execute("SELECT numero FROM Percha ORDER BY codigo__kayak ASC ")
            i=cursor.fetchall()
            cursor.execute("SELECT tipo,color FROM Kayak")
            o=cursor.fetchall()
            a=len(o)
            x=range(a)
            for numer in x:
                Tabla_kayak.insert("",tk.END,values=(i[numer]+o[numer]))
                


    def poner_clientes(): #COLOCA LOS CLIENTES EN LA CAJA
        conexion=sqlite3.connect("prueba.db")
        cursor=conexion.cursor()
        cursor.execute('SELECT apellidos, nombres FROM Clientes ORDER BY apellidos ASC')
        i=cursor.fetchall()     
        data= []
        for row in i:
            data.append(row)
        return data

        


    def buscar_kayak(): #BUSCADOR
            
                a =(lista_desplegable.get())
                value=a.split()
                print(value)
                print(len(value))
                guardar2 = Tabla_kayak.get_children() #obtener elementos de la tabla
                for element in guardar2:
                    Tabla_kayak.delete(element)
                conexion=sqlite3.connect("prueba.db")
                cursor=conexion.cursor()
                if len(value)<3: # SI UN NOMBRE TIENE 1 NOMBRE Y 1 APELLIDO UTILIZA ESTE CAMINO
                    cursor.execute("SELECT codigo_cliente FROM Clientes WHERE apellidos =('" + value[0]+ "') AND nombres =('" + value[1]+ "')") # WHERE type = "table" AND name = "employees"')
                    a=cursor.fetchone()
                    print(a)
                    b=functools.reduce(operator.add, (a)) #Utilizar esto en registro de clientes
                    c=str(b)
                    print(c)
                    cursor.execute("SELECT codigo_kayak FROM Kayak WHERE codigo__cliente=('" +c+ "')")
                    w=cursor.fetchall()
                    n=1
                    output=[w[i:i + n] for i in range(0, len(w), n)]
                    print(w)
                    
                    h=functools.reduce(operator.add, (output))
                    
                    j=functools.reduce(operator.add, (h))
                    f=str(j)
                    
                    def total_elements(list):
                        count = 0
                        for elementos in list:
                            count += 1
                        return count
                    # no funciona con más de un kayak//ARREGLADO
                    wo=(total_elements(w))
                    str1 = ' '.join(str(e) for e in j)
                    e=range(wo)

                    
                    for number in e:
                        a=str(j[number])
                        print(a)
                        cursor.execute("SELECT numero FROM Percha WHERE codigo__kayak=('"+a+"')")
                        o=cursor.fetchall()
                        cursor.execute("SELECT tipo FROM Kayak WHERE codigo_kayak=('"+a+"')")
                        l=cursor.fetchall()
                        cursor.execute("SELECT color FROM Kayak WHERE codigo_kayak=('"+a+"')")
                        x=cursor.fetchall()
                        print(l)
                        Tabla_kayak.insert("",tk.END,text=value, values=(o+l+x))


                else: # SI UN NOMBRE TIENE MÁS DE 1 NOMBRE O 1 APELLIDO UTILIZA ESTE CAMINO
                    characters="{","}"
                    for x in range(len(characters)):
                        a = a.replace(characters[x],"")    
                    print(a)
                    c=a.split(" ",2)
                    print(c)
                    s=c[0]+" "+c[1]
                    print(s)
                    cursor.execute("SELECT codigo_cliente FROM Clientes WHERE apellidos =('" +s+ "') AND nombres =('" + c[2]+ "')")
                    a=cursor.fetchone()
                    print(a)
                    b=functools.reduce(operator.add, (a)) #Utilizar esto en registro de clientes
                    g=str(b)
                    print(g)
                    cursor.execute("SELECT codigo_kayak FROM Kayak WHERE codigo__cliente=('" +g+ "')")
                    w=cursor.fetchall()
                    n=1
                    output=[w[i:i + n] for i in range(0, len(w), n)]
                    print(w)
                    
                    h=functools.reduce(operator.add, (output))
                    
                    j=functools.reduce(operator.add, (h))
                    f=str(j)
                    
                    def total_elements(list):
                        count = 0
                        for elementos in list:
                            count += 1
                        return count
                    # no funciona con más de un kayak
                    wo=(total_elements(w))
                    str1 = ' '.join(str(e) for e in j)
                    e=range(wo)

                    
                    for number in e:
                        a=str(j[number])
                        print(a)
                        cursor.execute("SELECT numero FROM Percha WHERE codigo__kayak=('"+a+"')")
                        o=cursor.fetchall()
                        #terminar
                        cursor.execute("SELECT tipo FROM Kayak WHERE codigo_kayak=('"+a+"')")
                        l=cursor.fetchall()
                        cursor.execute("SELECT color FROM Kayak WHERE codigo_kayak=('"+a+"')")
                        x=cursor.fetchall()
                        print(l)
                        Tabla_kayak.insert("",tk.END ,text=s+" "+c[2] ,values=(o+l+x))
                
                
            
                


#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------





    ventana3 = tk.Toplevel()

    ventana3.title("Prueba - perchas")

    ventana3['bg']='#fb0'

    frame=LabelFrame(ventana3,height=20, padx=200)
    frame.grid(row = 0,column=0, columnspan = 3 , pady=20, padx=20)

    lista_desplegable=ttk.Combobox(frame, state="readonly")
    lista_desplegable.grid(row=1, column=1)
    lista_desplegable["values"] = poner_clientes()




    Button(frame, text="Buscar kayaks",command= buscar_kayak).grid(row=1,column=0)
    Button(frame, text="Actualizar",command= poner_datos).grid(row=2,columnspan=2, sticky=W+E)

    Tabla_kayak=ttk.Treeview(ventana3,height=10, columns=('#1','#2','#3'))
    Tabla_kayak.grid(row=12, columnspan=5)
    Tabla_kayak.heading('#0' , text="Cliente", anchor=CENTER)
    Tabla_kayak.heading('#1' , text="Percha", anchor=CENTER)
    Tabla_kayak.heading('#2', text="Modelo Kayak", anchor=CENTER)
    Tabla_kayak.heading('#3', text="Color kayak", anchor=CENTER)
    
    

    poner_datos()







    ventana3.mainloop() 


#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
