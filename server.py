# import os
# from flask import Flask, send_from_directory, render_template, redirect,jsonify
# from flask_sqlalchemy import SQLAlchemy
# from flask_marshmallow import Marshmallow
# from flask_cors import CORS
# from sqlalchemy import text
# app = Flask(__name__)
# CORS(app)
# port = int(os.environ.get("PORT", 5000))
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://uwcz1z8tw0nrh0ey:OeX1Pjhhuve1VA5v0Pd8@bmotoxcjvbuzkz2ic55p-mysql.services.clever-cloud.com:3306/bmotoxcjvbuzkz2ic55p'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

# db=SQLAlchemy(app)
# ma=Marshmallow(app)


# @app.route('/',methods=['GET'])
# def home():
#     print("API CONECTADA")
#     query = text("SHOW TABLES;")
#     conn = db.engine.connect()
#     result = conn.execute(query)
#     column_names = result.keys()
#     # Construir una lista de diccionarios con los resultados
#     results_list = [dict(zip(column_names, row)) for row in result]
#     print("RESPONSE",results_list)
#     # Cerrar la conexión
#     conn.close()

#     # Retornar los resultados como JSON en la respuesta
#     return jsonify(results_list)
#     # Retornar los resultados como JSON en la respuesta
#     #return jsonify("Api Conectada")

# @app.route('/aire',methods=['GET'])
# def aire():
#     # Obtener una conexión a la base de datos
#     conn = db.engine.connect()

#     # Realizar la consulta SELECT *
#     query = text("SELECT * FROM Aire")
#     result = conn.execute(query)
#     column_names = result.keys()

#     # Construir una lista de diccionarios con los resultados
#     results_list = [dict(zip(column_names, row)) for row in result]
#     # Cerrar la conexión
#     conn.close()

#     # Retornar los resultados como JSON en la respuesta
#     return jsonify(results_list)

# @app.route('/ilumina',methods=['GET'])
# def ilumina():
#     # Obtener una conexión a la base de datos
#     conn = db.engine.connect()

#     # Realizar la consulta SELECT *
#     query = text("SELECT * FROM Iluminacion")
#     result = conn.execute(query)
#     column_names = result.keys()

#     # Construir una lista de diccionarios con los resultados
#     results_list = [dict(zip(column_names, row)) for row in result]
#     # Cerrar la conexión
#     conn.close()

#     # Retornar los resultados como JSON en la respuesta
#     return jsonify(results_list)

# @app.route('/tempe',methods=['GET'])
# def tempe():
#     # Obtener una conexión a la base de datos
#     conn = db.engine.connect()

#     # Realizar la consulta SELECT *
#     query = text("SELECT * FROM Temperatura")
#     result = conn.execute(query)
#     column_names = result.keys()

#     # Construir una lista de diccionarios con los resultados
#     results_list = [dict(zip(column_names, row)) for row in result]
#     # Cerrar la conexión
#     conn.close()

#     # Retornar los resultados como JSON en la respuesta
#     return jsonify(results_list)

# @app.route('/actual',methods=['GET'])
# def actual():
#     # Obtener una conexión a la base de datos
#     conn = db.engine.connect()

#     # Realizar la consulta SELECT *
#     query = text("SELECT * FROM actual order by id desc limit 1")
#     result = conn.execute(query)
#     column_names = result.keys()
#     # Construir una lista de diccionarios con los resultados
#     results_list = [dict(zip(column_names, row)) for row in result]
#     # Cerrar la conexión
#     conn.close()

#     # Retornar los resultados como JSON en la respuesta
#     return jsonify(results_list[0])

# if __name__ == "__main__":
#     app.run(port=port)

from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from sqlalchemy import text
import mysql.connector
app=Flask(__name__)
CORS(app)
#app.config['SQL_ALCHEMY_DATABASE_URI']='sqlite:///database.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://uioqtyvifbcq4uvd:nsc7lCQOKwlgg6czKDR@bdmwjg39hmizh6g572f1-mysql.services.clever-cloud.com:20109/bdmwjg39hmizh6g572f1'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)
ma=Marshmallow(app)

@app.route('/',methods=['GET'])
def home():
    print("API CONECTADA")

    # Retornar los resultados como JSON en la respuesta
    return jsonify("Api Conectada")

@app.route('/actual',methods=['GET'])
def actual():
    # Obtener una conexión a la base de datos
    conn = db.engine.connect()
    parameter1 = request.args.get('id')
    print(parameter1,"id")
    # Realizar la consulta SELECT *
    query = text("SELECT * FROM actual WHERE id="+parameter1)
    result = conn.execute(query)
    column_names = result.keys()

    # Construir una lista de diccionarios con los resultados
    results_list = [dict(zip(column_names, row)) for row in result]
    # Cerrar la conexión
    conn.close()

    # Retornar los resultados como JSON en la respuesta
    return jsonify(results_list)

connection = mysql.connector.connect(
    user='uioqtyvifbcq4uvd',
    password='nsc7lCQOKwlgg6czKDR',
    host='bdmwjg39hmizh6g572f1-mysql.services.clever-cloud.com',
    database='bdmwjg39hmizh6g572f1',
    port='20109'
)

@app.route('/encender_vent1',methods=['GET'])
def encender_vent1():
    cursor = connection.cursor()  
    sql = "INSERT INTO Temperatura (Ventilacion) VALUES (1)"
    cursor.execute(sql) 
    connection.commit() 
    # Cerrar la conexión
    cursor.close()

    # Retornar los resultados como JSON en la respuesta
    return jsonify()

@app.route('/encender_vent2',methods=['GET'])
def encender_vent2():
    cursor = connection.cursor()  
    sql = "INSERT INTO Temperatura (Ventilacion) VALUES (2)"
    cursor.execute(sql) 
    connection.commit() 
    # Cerrar la conexión
    cursor.close()

    # Retornar los resultados como JSON en la respuesta
    return jsonify()

@app.route('/apagar_vent',methods=['GET'])
def apagar_vent():
    cursor = connection.cursor()  
    sql = "INSERT INTO Temperatura (Ventilacion) VALUES (0)"
    cursor.execute(sql) 
    connection.commit() 
    # Cerrar la conexión
    cursor.close()

    # Retornar los resultados como JSON en la respuesta
    return jsonify()

@app.route('/encender_luz',methods=['GET'])
def encender_luz():
    # Obtener una conexión a la base de datos
    conn = db.engine.connect()

    # Realizar la consulta SELECT *
    query = text("SELECT * FROM actual ORDER BY actual.id DESC LIMIT 1")
    result = conn.execute(query)
    column_names = result.keys()

    # Construir una lista de diccionarios con los resultados
    results_list = [dict(zip(column_names, row)) for row in result]
    print(results_list)
    # Cerrar la conexión
    conn.close()

    Presencia_Humana_value = results_list[0]['Presencia_Humana']
    #se puede realizar operaciones
    if Presencia_Humana_value == 1 :
        cursor = connection.cursor()  
        sql = "INSERT INTO Iluminacion (Iluminacion_habitacion,Iluminacion_activa_1,Iluminacion_activa_2) VALUES (%s,%s,%s)"
        cursor.execute(sql,(1,0,0)) 
        connection.commit() 
        # Cerrar la conexión
        conn.close()
        cursor.close()

    # Retornar los resultados como JSON en la respuesta
    return jsonify(results_list[0])

@app.route('/apagar_luz',methods=['GET'])
def apagar_luz():
    # Obtener una conexión a la base de datos
    conn = db.engine.connect()

    # Realizar la consulta SELECT *
    query = text("SELECT * FROM actual ORDER BY id DESC LIMIT 1")
    result = conn.execute(query)
    column_names = result.keys()

    # Construir una lista de diccionarios con los resultados
    results_list = [dict(zip(column_names, row)) for row in result]
    print(results_list)
    # Cerrar la conexión
    conn.close()

    Presencia_Humana_value = results_list[0]['Presencia_Humana']
    #se puede realizar operaciones
    if Presencia_Humana_value == 1:
        cursor = connection.cursor()  
        sql = "INSERT INTO Iluminacion (Iluminacion_habitacion,Iluminacion_activa_1,Iluminacion_activa_2) VALUES (%s,%s,%s)"
        cursor.execute(sql,(0,0,0)) 
        connection.commit() 
        # Cerrar la conexión
        #conn.close()
        cursor.close()

    # Retornar los resultados como JSON en la respuesta
    return jsonify(results_list[0])


@app.route('/notificacion',methods=['GET'])
def notificacion():    
    data={
        "aire1":0,
        "aire2":0,
        "luz1":0,
        "luz2":0
    }
    # Obtener una conexión a la base de datos
    conn = db.engine.connect()

    # Realizar la consulta notificaicon aire
    query = text("SELECT * FROM Aire ORDER BY id DESC LIMIT 1")
    result = conn.execute(query)
    column_names = result.keys()
    # Construir una lista de diccionarios con los resultados
    results_list = [dict(zip(column_names, row)) for row in result]
    aire_habitacion_1_value = results_list[0]['aire_habitacion_1']
    aire_habitacion_2_value = results_list[0]['aire_habitacion_2']
    
    # Realizar la consulta notificaicon aire
    query = text("SELECT * FROM Iluminacion ORDER BY id DESC LIMIT 1")
    result = conn.execute(query)
    column_names = result.keys()
    # Construir una lista de diccionarios con los resultados
    results_list = [dict(zip(column_names, row)) for row in result]
    print(results_list)
    iluminacion_habitacion_value = results_list[0]['Iluminacion_habitacion']
    iluminacion_activa_1_value = results_list[0]['Iluminacion_activa_1']
    iluminacion_activa_2_value = results_list[0]['Iluminacion_activa_2']

    #validaciones aire
    if  aire_habitacion_1_value == 1 or aire_habitacion_2_value ==1:
        cursor = connection.cursor()  
        sql = "INSERT INTO aire (aire_habitacion_1,aire_habitacion_2) VALUES (%s,%s)"
        cursor.execute(sql,(0,0)) 
        connection.commit() 
        # Cerrar la conexión
        conn.close()
        cursor.close()
        if aire_habitacion_1_value == 1: 
            data["aire1"]=1
            #aire deficiente
            cursor = connection.cursor()
            sql = "INSERT INTO Notificaciones (aviso) VALUES (%s)"
            cursor.execute(sql,("La habitacion cuenta con una calidad de aire deficiente")) 
            connection.commit() 
            # Cerrar la conexión
            conn.close()
            cursor.close()
        else:
            data["aire2"]=1
            #aire optimo
            cursor = connection.cursor()
            sql = "INSERT INTO Notificaciones (aviso) VALUES (%s)"
            cursor.execute(sql,("La habitacion posee una calidad de aire optima")) 
            connection.commit() 
            # Cerrar la conexión
            conn.close()
            cursor.close()
    #validaciones iluminacion
    if  iluminacion_activa_1_value == 1 or iluminacion_activa_2_value ==1:
        cursor = connection.cursor()  
        sql = "INSERT INTO Iluminacion (Iluminacion_habitacion,Iluminacion_activa_1,Iluminacion_activa_2) VALUES (%s,%s,%s)"
        cursor.execute(sql,(iluminacion_habitacion_value,0,0)) 
        connection.commit() 
        # Cerrar la conexión
        conn.close()
        cursor.close()
        if iluminacion_activa_1_value == 1: 
            data["luz1"]=1
            #habitacion encendida
            cursor = connection.cursor()
            sql = "INSERT INTO Notificaciones (aviso) VALUES (%s)"
            cursor.execute(sql,("La habitacion esta iluminada pero no hay presencia humana")) 
            connection.commit() 
            # Cerrar la conexión
            conn.close()
            cursor.close()
        else:
            data["luz2"]=1
            #habitacion apagada
            cursor = connection.cursor()
            sql = "INSERT INTO Notificaciones (aviso) VALUES (%s)"
            cursor.execute(sql,("El sistema de iluminacion ha sido apagado")) 
            connection.commit() 
            # Cerrar la conexión
            conn.close()
            cursor.close() 
    data={
        "aire1":0,
        "aire2":0,
        "luz1":0,
        "luz2":0
    }
    # Obtener una conexión a la base de datos
    conn = db.engine.connect()

    # Realizar la consulta notificaicon aire
    query = text("SELECT * FROM Aire ORDER BY id DESC LIMIT 1")
    result = conn.execute(query)
    column_names = result.keys()
    # Construir una lista de diccionarios con los resultados
    results_list = [dict(zip(column_names, row)) for row in result]
    aire_habitacion_1_value = results_list[0]['aire_habitacion_1']
    aire_habitacion_2_value = results_list[0]['aire_habitacion_2']
    
    # Realizar la consulta notificaicon aire
    query = text("SELECT * FROM Iluminacion ORDER BY id DESC LIMIT 1")
    result = conn.execute(query)
    column_names = result.keys()
    # Construir una lista de diccionarios con los resultados
    results_list = [dict(zip(column_names, row)) for row in result]
    print(results_list)
    iluminacion_habitacion_value = results_list[0]['Iluminacion_habitacion']
    iluminacion_activa_1_value = results_list[0]['Iluminacion_activa_1']
    iluminacion_activa_2_value = results_list[0]['Iluminacion_activa_2']

    #validaciones aire
    if  aire_habitacion_1_value == 1 or aire_habitacion_2_value ==1:
        cursor = connection.cursor()  
        sql = "INSERT INTO aire (aire_habitacion_1,aire_habitacion_2) VALUES (%s,%s)"
        cursor.execute(sql,(0,0)) 
        connection.commit() 
        # Cerrar la conexión
        conn.close()
        cursor.close()
        if aire_habitacion_1_value == 1: 
            data["aire1"]=1
        else:
            data["aire2"]=1
    #validaciones iluminacion
    if  iluminacion_activa_1_value == 1 or iluminacion_activa_2_value ==1:
        cursor = connection.cursor()  
        sql = "INSERT INTO Iluminacion (Iluminacion_habitacion,Iluminacion_activa_1,Iluminacion_activa_2) VALUES (%s,%s,%s)"
        cursor.execute(sql,(iluminacion_habitacion_value,0,0)) 
        connection.commit() 
        # Cerrar la conexión
        conn.close()
        cursor.close()
        if iluminacion_activa_1_value == 1: 
            data["luz1"]=1
        else:
            data["luz2"]=1
    

    # Cerrar la conexión
    conn.close()
    
    #print(data)
    # Retornar los resultados como JSON en la respuesta
    return jsonify(data)

@app.route('/notificaciones',methods=['GET'])
def notificaciones():
    # Obtener una conexión a la base de datos
    conn = db.engine.connect()

    # Realizar la consulta SELECT *
    query = text("SELECT * FROM Notificaciones")
    result = conn.execute(query)
    column_names = result.keys()

    # Construir una lista de diccionarios con los resultados
    results_list = [dict(zip(column_names, row)) for row in result]
    # Cerrar la conexión
    conn.close()

    # Retornar los resultados como JSON en la respuesta
    return jsonify(results_list)


if __name__=='__main__':
    app.run(debug=True,host="0.0.0.0")
