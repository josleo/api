from typing import Union

from fastapi import FastAPI
import mysql.connector
app = FastAPI()


@app.get("/")
def read_root():
    list = ["pregunta 1 -- Año con más carreras-- https://henrry-n1.herokuapp.com/tres",
            "pregunta 1 -- Año con más carreras-- https://henrry-n1.herokuapp.com/tres"]
    return (list)





#se crea un funcuion para mostrar los datos de la primera pregunta " Año con más carreras "
@app.get("/uno")
def  uno():
    miConexion = mysql.connector.connect( host="estacion.educatics.org",
                                          user= 'educaics_usr_est',
                                          passwd='F5z!xZ5jhSyg', 
                                          db="educaics_db_estacion"  )  
    cur = miConexion.cursor()
    cur.execute("select * from pregunta1" )
    datos = [row for row in cur.fetchall()]
    miConexion.close()
    return (datos)


#Piloto con mayor cantidad de primeros puestos
@app.get("/dos")
def  dos():
    miConexion = mysql.connector.connect( host="estacion.educatics.org",
                                          user= 'educaics_usr_est',
                                          passwd='F5z!xZ5jhSyg', 
                                          db="educaics_db_estacion" )     
    cur = miConexion.cursor()
    cur.execute("select  * from pregunta2" )
    datos2 = [row for row in cur.fetchall()]
    miConexion.close()
    return (datos2)


#Nombre del circuito más corrido
@app.get("/tres")
def  tres():

    miConexion = mysql.connector.connect( host="estacion.educatics.org",
                                          user= 'educaics_usr_est',
                                          passwd='F5z!xZ5jhSyg', 
                                          db="educaics_db_estacion"  )  
    cur = miConexion.cursor()
    cur.execute("select * from pregunta3")
    datos3 = [row for row in cur.fetchall()]
    miConexion.close()
    return (datos3)


#Piloto con mayor cantidad de puntos en total, cuyo constructor sea de nacionalidad sea American o British
@app.get("/cuatro")
def  cuatro():
    miConexion = mysql.connector.connect( host="estacion.educatics.org",
                                          user= 'educaics_usr_est',
                                          passwd='F5z!xZ5jhSyg', 
                                          db="educaics_db_estacion"  )  
    cur = miConexion.cursor()
    cur.execute("select  * from pregunta4" )
    datos4 = [row for row in cur.fetchall()]
    miConexion.close()
    return (datos4)
