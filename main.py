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
    cur.execute("SELECT MAX(gan.driver) as ' carreras ganadas', gan.driverId as piloto, d.name as Nombre FROM (SELECT driverId, COUNT(driverId) as driver FROM results WHERE positionOrder='1' GROUP BY driverId) gan JOIN drivers d  ON (gan.driverId=d.driverId);" )
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

@app.get("/europa")
def  uno():
    db = mysql.connector.connect(host='database-1.cmmt68xsoykx.us-east-1.rds.amazonaws.com',
                                        user='admin',
                                        passwd='123456789',
                                        db='sys',
                                        port=3306)

   
# This line is that you need
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM europa ")
    result = cursor.fetchall()
    datos= (f"europa: {json.dumps(result)}")
    db.close()
    return (datos)
