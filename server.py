import os
from flask import Flask, send_from_directory, render_template, redirect,jsonify
from flask_cors  import CORS
app = Flask(__name__)
CORS(app)
port = int(os.environ.get("PORT", 5000))

@app.route('/',methods=['GET'])
def home():
    print("API CONECTADA")

    # Retornar los resultados como JSON en la respuesta
    return jsonify("Api Conectada")
    return redirect('/')

if __name__ == "__main__":
    app.run(port=port)