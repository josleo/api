from typing import Union

from fastapi import FastAPI
import mysql.connector
app = FastAPI()


@app.get("/")
def read_root():
    list = ["pregunta 1 -- Año con más carreras-- https://henrry-n1.herokuapp.com/uno",
            "pregunta 2 -- Año con más carreras-- https://henrry-n1.herokuapp.com/dos"
            "pregunta 2 -- Año con más carreras-- https://henrry-n1.herokuapp.com/tres"]
    return (list)
    

#se crea un funcuion para mostrar los datos de la primera pregunta " Año con más carreras "
@app.get("/uno")
def  uno():
    miConexion = mysql.connector.connect( host="ace.com.pe",
                                          user= 'acecompe_prueba1',
                                          passwd='.&ve3Z5_VJW0', 
                                          db="acecompe_prueba1"  )  
                                         
    cur = miConexion.cursor()
    cur.execute("select * from pregunta1" )
    datos = [row for row in cur.fetchall()]
    miConexion.close()
    return (datos)


#Piloto con mayor cantidad de primeros puestos
@app.get("/dos")
def  dos():
    miConexion = mysql.connector.connect( host="ace.com.pe",
                                          user= 'acecompe_prueba1',
                                          passwd='.&ve3Z5_VJW0', 
                                          db="acecompe_prueba1"  )     
    cur = miConexion.cursor()
    cur.execute("SELECT MAX(gan.driver) as ' carreras ganadas', gan.driverId as piloto, d.name as Nombre FROM (SELECT driverId, COUNT(driverId) as driver FROM results WHERE positionOrder='1' GROUP BY driverId) gan JOIN drivers d  ON (gan.driverId=d.driverId);" )
    datos2 = [row for row in cur.fetchall()]
    miConexion.close()
    return (datos2)


#Nombre del circuito más corrido
@app.get("/tres")
def  tres():
    miConexion = mysql.connector.connect( host="ace.com.pe",
                                          user= 'acecompe_prueba1',
                                          passwd='.&ve3Z5_VJW0', 
                                          db="acecompe_prueba1"  )  
    cur = miConexion.cursor()
    cur.execute("select * from pregunta3")
    datos3 = [row for row in cur.fetchall()]
    miConexion.close()
    return (datos3)


#Piloto con mayor cantidad de puntos en total, cuyo constructor sea de nacionalidad sea American o British
@app.get("/cuatro")
def  cuatro():
    miConexion = mysql.connector.connect( host="ace.com.pe",
                                          user= 'acecompe_prueba1',
                                          passwd='.&ve3Z5_VJW0', 
                                          db="acecompe_prueba1"  )  
    cur = miConexion.cursor()
    cur.execute("select  * from pregunta4" )
    datos4 = [row for row in cur.fetchall()]
    miConexion.close()
    return (datos4)
