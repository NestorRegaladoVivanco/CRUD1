import mysql.connector

bd = mysql.connector.connect(
    user = 'nestor',password = 'pootis',
    database='cinemapp')

cursor = bd.cursor()

def get_usuarios():
    consulta = "SELECT * FROM usuario"

    cursor.execute(consulta)
    usuarios = []
    for row in cursor.fetchall():
        usuario = {
            'id': row[0],
            'correo': row[1],
            'contrasena': row[2]
        }
        usuarios.append(usuario)
    return usuarios

def existe_usuario(correo):
    query = "SELECT COUNT(*) FROM usuario WHERE correo = %s"
    cursor.execute(query,(correo,))

    if cursor.fetchone()[0] == 1:
        return True
    else:
        return False

import hashlib
def crear_usuario(correo, contra):
    if existe_usuario(correo):
        return False
    else:
        h = hashlib.new('sha256',bytes(contra, 'utf-8'))
        h = h.hexdigest()
        insertar = "INSERT INTO usuario(correo, contrasena) VALUES(%s,%s)"
        cursor.execute(insertar,(correo,h))
        bd.commit()

        return True

def iniciar_sesion(correo, contra):
    h = hashlib.new('sha256',bytes(contra, 'utf-8'))
    h = h.hexdigest()
    query = "SELECT id FROM usuario WHERE correo = %s AND contrasena = %s"
    cursor.execute(query,(correo, h))
    id = cursor.fetchone()
    if id:
        return id[0], True
    else:
        return None, False