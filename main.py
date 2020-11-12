from flask import Flask, jsonify, request

from conexion import crear_usuario, iniciar_sesion
from conexion import insertar_peliculas,get_peliculas

app = Flask(__name__)

@app.route("/api/v1/usuarios", methods = ["POST"])
def usuario():
    if request.method == "POST" and request.is_json :
        try:
            data = request.get_json()
            print(data)

            if crear_usuario(data['correo'],data['contrasena']):
                return jsonify({"code":"ok"})
            else:
                return jsonify({"code":"existe"})
        except:
            return jsonify({"code": "error"})

@app.route("/api/v1/peliculas", methods = ["GET","POST"])
def peliculas():
    if request.method == "POST" and request.is_json:
        try:
            data = request.get_json()
            print(data)
            if insertar_peliculas(data):
                return jsonify({"code":"ok"})
            else:
                return jsonify({"code":"no"})
        except:
            return jsonify({"code":"error"})
    elif request.method == "GET":
        return jsonify(get_peliculas())


@app.route("/api/v1/sesiones", methods=["POST"])
def sesion():
    if request.method == "POST" and request.is_json:
        try:
            data = request.get_json()
            correo = data['correo']
            contra = data['contrasena']
            id, ok =iniciar_sesion(correo,contra)
            if ok:
                return jsonify({"code":"ok","id":id})
            else:
                return jsonify({"code":"no existe"})
        except:
            return jsonify({"code":"error"})
app.run(debug=True)