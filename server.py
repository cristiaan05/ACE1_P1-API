import os
from flask import Flask, send_from_directory, render_template, redirect,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from sqlalchemy import text
app = Flask(__name__)
CORS(app)
port = int(os.environ.get("PORT", 5000))
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://uwcz1z8tw0nrh0ey:OeX1Pjhhuve1VA5v0Pd8@bmotoxcjvbuzkz2ic55p-mysql.services.clever-cloud.com:3306/bmotoxcjvbuzkz2ic55p'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)
ma=Marshmallow(app)


@app.route('/',methods=['GET'])
def home():
    print("API CONECTADA")

    # Retornar los resultados como JSON en la respuesta
    return jsonify("Api Conectada")

@app.route('/night',methods=['GET'])
def night():
    # Obtener una conexión a la base de datos
    conn = db.engine.connect()

    # Realizar la consulta SELECT *
    query = text("SELECT * FROM noche")
    result = conn.execute(query)
    column_names = result.keys()

    # Construir una lista de diccionarios con los resultados
    results_list = [dict(zip(column_names, row)) for row in result]
    # Cerrar la conexión
    conn.close()

    # Retornar los resultados como JSON en la respuesta
    return jsonify(results_list)

if __name__ == "__main__":
    app.run(port=port)