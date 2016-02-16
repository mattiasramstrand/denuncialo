"""
This file sets up the tables and get, post, put, delete functions with the database. 
These functions is called in the api.py file. 
"""

from datetime import datetime, timedelta
from io import BytesIO
from FlaskWebProject import app
from datetime import datetime, timedelta
from flask import g, jsonify
from flask import request
from flask_restful import reqparse, abort, Api, Resource
from defaultvalues import *
import sqlite3, json, base64, PIL, random, string, math
from PIL import Image
from base64 import decodestring



"""
Sqlite3 works with having a database file locally which is later pushed up to 
the server. Not sure if we can use this way of setup in our thesis.
Hopefully we can, it's much easier.
"""
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('database.db')
        db.row_factory = sqlite3.Row
    return db

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def decode_base64(data):
    missing_padding = 4 - len(data) % 4
    if missing_padding:
        data += b'='* missing_padding
    return base64.decodestring(data)

def download_file(filename):
    return send_from_directory("static/denuncia_img",
                               filename,)


"""
These functions makes the tables with information in the database.
In every function you need the cursor to access the database.
"""
def create_denuncia_table():
    with app.app_context():
        cur = get_db().cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS denuncias(
            'id' INTEGER PRIMARY KEY,
            'idUsuario' TEXT,
            'fecha' TEXT,
            'titulo' TEXT,
            'descripcion' TEXT,
            'categoria' TEXT,
            'imagenSmall' TEXT,
            'imagenBig' TEXT, 
            'latitud' REAL,
            'longitud' REAL,
            'direccion' TEXT,
            'codigoPostal' REAL,
            'apoyos' INT DEFAULT 0, 
            'visualizaciones' INT DEFAULT 0,
            'totalComentarios' INT DEFAULT 0,
            'totalReportes' INT DEFAULT 0, 
            'fechaModificacion' TEXT,
            'estado' TEXT DEFAULT 'Publicada')''')
        cur.close()

def create_comentario_table():
    with app.app_context():
        cur = get_db().cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS comentarios (
            'id' INTEGER PRIMARY KEY,
            'idDenuncia' INT,
            'idUsuario' TEXT,
            'fecha' TEXT,
            'mensaje' TEXT)''')
        cur.close()

def create_usuario_table():
    with app.app_context():
        cur = get_db().cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS usuario(
            'idUsuario' TEXT PRIMARY KEY,
            'telefono' TEXT DEFAULT '+34 XXX XX XX XX',
            'imagenAvatar' TEXT DEFAULT 'http://denuncialo.azurewebsites.net/static/usuario_img/logo.jpg',
            'nombre' TEXT DEFAULT 'Tester', 
            'email' TEXT DEFAULT 'tester@inf.upv.es',
            'notificacionesGeneral' INTEGER DEFAULT 0, 
            'notificacionesEstado' INTEGER DEFAULT 0,
            'notificacionesComentarios' INTEGER DEFAULT 0)''')
        cur.close()


"""
Apoyo means support in spanish. This table works like the facebook
like button. 
"""
def create_apoyo_table():
    with app.app_context():
        cur = get_db().cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS apoyo(
            'idApoyo' INTEGER PRIMARY KEY,
            'idDenuncia' INT,
            'idUsuario' INT)''')
        cur.close()

def create_reporte_table():
    with app.app_context():
        cur = get_db().cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS reporte(
            'idReporte' INTEGER PRIMARY KEY,
            'idDenuncia' INT,
            'idUsuario' INT)''')
        cur.close()

def create_administrador_table():
    with app.app_context():
        cur = get_db().cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS administrador(
            'idAdmin' INTEGER PRIMARY KEY,
            'usuario' INT,
            'clave' TEXT,
            'email' TEXT)''')
        cur.close()


"""
Theese add functions is used to add information to the database. They are
only used in the code itself. Not called from the user. There is some
examples at the bottom of this file. The information they take in as 
input is called from defaultvalues.py
"""
def add_Administrador(idAdmin=None, usuario=None, clave=None, email=None):
    cur = get_db().cursor()
    fecha = str(datetime.now() + timedelta(hours=2))[:-7] 
    cur.execute('''INSERT INTO administrador(idAdmin, usuario, clave, email)
            VALUES (?,?,?)''',(idAdmin, usuario, clave, email))
    cur.close()


def add_reporte(idReporte=None, idDenuncia=None, idUsuario=None):
    cur = get_db().cursor()
    fecha = str(datetime.now() + timedelta(hours=2))[:-7] 
    cur.execute('''INSERT INTO reporte(idReporte, idDenuncia, idUsuario)
            VALUES (?,?,?)''',(idReporte, idDenuncia, idUsuario))
    cur.close()


def add_apoyo(idApoyo=None, idDenuncia=None, idUsuario=None):
    cur = get_db().cursor()
    fecha = str(datetime.now() + timedelta(hours=2))[:-7] 
    cur.execute('''INSERT INTO apoyo(idApoyo, idDenuncia, idUsuario)
            VALUES (?,?,?)''',(idApoyo, idDenuncia, idUsuario))
    cur.close()


def add_usuario(idUsuario=None, telefono=None, imagenAvatar=None, nombre=None,
                email=None, notificacionesGeneral=None, notificacionesEstado=None, notificacionesComentarios=None):
    cur = get_db().cursor()
    cur.execute('''INSERT INTO usuario(idUsuario, telefono, imagenAvatar, nombre,
                                                 email, notificacionesGeneral, notificacionesEstado, notificacionesComentarios)
            VALUES (?,?,?,?,?,?,?,?)''',(idUsuario, telefono, imagenAvatar, nombre,
                                                 email, notificacionesGeneral, notificacionesEstado, notificacionesComentarios))
    cur.close()


def add_comentario(id=None, idDenuncia=None, idUsuario=None, fecha=None, nombre=None, imagen=None, mensaje=None, comentarioMio=1):
    #fecha = str(datetime.now())[:-7]
    cur = get_db().cursor()
    fecha = str(datetime.now() + timedelta(hours=2))[:-7] 
    cur.execute('''INSERT INTO comentarios(id, idDenuncia, idUsuario, fecha, mensaje)
            VALUES (?,?,?,?,?)''',(id, idDenuncia, idUsuario, fecha, mensaje))
    cur.close()


def add_denuncia(id=None, idUsuario=None, fecha=None, titulo=None, descripcion=None, categoria=None, imagenSmall=None, 
                    imagenBig=None, longitud=0, latitud=0, codigoPostal=0, direccion=None, apoyos=None, visualizaciones=0, 
                    totalComentarios=0, totalReportes=0, fechaModificacion=None, estado=None):
    #fecha = str(datetime.now() + timedelta(hours=2))[:-7] 
    cur = get_db().cursor()
    cur.execute('''INSERT INTO denuncias(id, idUsuario, fecha, titulo, descripcion, categoria, imagenSmall, imagenBig, 
                                        longitud, latitud, codigoPostal,direccion, apoyos, 
                                        visualizaciones, totalComentarios, totalReportes, fechaModificacion, estado)
        VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(id, idUsuario, fecha, titulo, descripcion, categoria, imagenSmall, 
                                                            imagenBig, longitud, latitud, codigoPostal,direccion,
                                                            apoyos, visualizaciones, totalComentarios, totalReportes, 
                                                            fechaModificacion, estado))
    cur.close()



"""
Here is different kinds of get, post, put, delete functions
for all kinds of tables. Theese functions is called in upon in
api.py. Important functions. :)
""" 
def get_denuncialist(args): 
    query = '''SELECT id as idDenuncia, idUsuario, fecha, titulo, descripcion, latitud, longitud, imagenBig as imagen,
                    apoyos, totalComentarios, visualizaciones, categoria, estado FROM denuncias'''
    radius = 0.0028
    if args.filter == "cercanas":
        query += " WHERE latitud > {} AND latitud < {} AND longitud > {} AND longitud < {}".format(float(args.latitud)-radius, 
                                                                                                   float(args.latitud)+radius,
                                                                                                   float(args.longitud)-radius,
                                                                                                   float(args.longitud)+radius)
    if args.filter in ("apoyos", "visualizaciones", "fecha"):
        query += " ORDER BY " + args.filter + " DESC"
    cur = get_db().cursor()
    all_denuncias = cur.execute(query).fetchall()
    denuncias = [dict(d) for d in all_denuncias]
    cur.close()
    return denuncias


def get_listaduplicados(listaDenuncias,denuncia):
    if(len(listaDenuncias)<=1):
        return []
    listaDuplicados = []
    distanciaMin = 0.000278*2
    x1 = denuncia['latitud']
    y1 = denuncia['longitud']
    for i in range(0,len(listaDenuncias)):
        aux = listaDenuncias[i]
        if((aux['idDenuncia'] != denuncia['idDenuncia']) and (aux not in listaDuplicados)):
            x2 = aux['latitud']
            y2 = aux['longitud']
            distancia = math.sqrt(math.pow(x1-x2,2)+math.pow(y1-y2,2))
            if(distancia <= distanciaMin):
                listaDuplicados.append(aux)
    return listaDuplicados


def post_denuncialist(args):
    file_key = id_generator()
    fecha = str(datetime.now() + timedelta(hours=1))[:-7]
    # file_path_big = 'FlaskWebProject/static/denuncias_img/{}_big.jpg'.format(file_key)
    # # file_path_small = 'imagen/{}_small.jpg'.format(file_key)
    # args.imagen = args.imagen[args.imagen.find(",")+1:]
    # with open(file_path_big, "w") as file:
    #     file.write(decode_base64(args.imagen))
    # imagenBig = 'FlaskWebProject/static/denuncias_img/{}_big.jpg'.format(file_key)
    # imagenSmall = 'FlaskWebProject/static/denuncias_img/{}_big.jpg'.format(file_key)
    # # imagenBig = download_file('{}_big.jpg'.format(file_key))
    cur = get_db().cursor()
    cur.execute('''INSERT INTO denuncias(titulo, descripcion, categoria, imagenSmall, imagenBig,
                                        latitud, longitud, fecha, direccion, codigoPostal, idUsuario
                ) VALUES (?,?,?,?,?,?,?,?,?,?,?)''',
        (args.titulo, args.descripcion, args.categoria, args.imagen, args.imagen, args.latitud, args.longitud, 
        fecha, args.direccion, args.codigoPostal, args.idUsuario))
    cur.close()
    return '', 201


def get_denuncia(denuncia_id, args):
    cur = get_db().cursor()
    denuncia = cur.execute('''SELECT id as idDenuncia, idUsuario as idDenunciante, titulo, estado, descripcion, latitud, longitud, 
                                    fecha, direccion, apoyos, imagenBig as imagen, totalComentarios as comentarios,
                                    categoria FROM denuncias WHERE id=?''',([denuncia_id])).fetchone()
    if denuncia == None:
        return {}, 200

    denuncia = dict(denuncia)
    usuario = cur.execute('''SELECT nombre, imagenAvatar FROM usuario WHERE idUsuario=?''',(denuncia['idDenunciante'],)).fetchone()
    usuario = dict(usuario)
    denuncia['nombreDenunciante'] = usuario['nombre']
    denuncia['avatarDenunciante'] = usuario['imagenAvatar'] 

    if args["Auth-Token"]:
        _reporte = cur.execute('''SELECT idDenuncia, idUsuario FROM reporte 
                                 WHERE idDenuncia=? AND idUsuario=?''',(denuncia_id, args["Auth-Token"],)).fetchone()
        denuncia['reportadaPorMi'] = '0' if _reporte == None else '1'
        _apoyo = cur.execute('''SELECT idDenuncia, idUsuario FROM apoyo
                                 WHERE idDenuncia=? AND idUsuario=?''',(denuncia_id, args["Auth-Token"],)).fetchone()
        denuncia['apoyadaPorMi'] = '0' if _apoyo == None else '1'
        print _apoyo
    if args["Auth-Token"] == denuncia["idDenunciante"]:
        denuncia['denunciaMia'] = '1'
    else:
        denuncia['denunciaMia'] = '0'
    cur.close()
    if denuncia:
        return denuncia
    return {}, 404


def delete_denuncia(denuncia_id, args):
    cur = get_db().cursor()
    _idUsuario = cur.execute('''SELECT idUsuario FROM denuncias WHERE id=?''',(denuncia_id,)).fetchone()[0]
    if args["Auth-Token"] == _idUsuario:
        cur.execute('DELETE FROM denuncias WHERE id=?', (denuncia_id,))
    cur.close()
    return ''

        
def put_denuncia(denuncia_id, args):
    cur = get_db().cursor()
    _idUsuario = cur.execute('''SELECT idUsuario FROM denuncias WHERE id=?''',(denuncia_id,)).fetchone()[0]
    if args["Auth-Token"] == _idUsuario:
        cur.execute('UPDATE denuncias SET titulo=?, descripcion=?, categoria=? WHERE id=?',
            (args.titulo, args.descripcion, args.categoria, denuncia_id))
    denuncia = cur.execute('SELECT * FROM denuncias WHERE id=?', (denuncia_id,)).fetchone()
    cur.close()
    return dict(denuncia)


def get_comentariolist(denuncia_id):
    cur = get_db().cursor()
    all_comentarios = cur.execute('''SELECT c.id as idComentario, c.fecha as fecha, c.idUsuario as idUsuario, c.mensaje as mensaje,
                                    u.imagenAvatar as imagenAvatar, u.nombre as nombreUsuario
                                    FROM comentarios c
                                    LEFT JOIN usuario u on u.idUsuario = c.idUsuario
                                    WHERE c.idDenuncia=?
                                    GROUP BY c.id ORDER BY c.id DESC''',(denuncia_id)).fetchall()
    cur.close()
    return [dict(d) for d in all_comentarios]


def post_comentariolist(denuncia_id, args):
    fecha = str(datetime.now() + timedelta(hours=1))[:-7] 
    cur = get_db().cursor()
    cur.execute('''INSERT INTO comentarios(idDenuncia, idUsuario, mensaje, fecha) VALUES (?,?,?,?)''',(denuncia_id, args.idUsuario, args.mensaje, fecha))
    cur.execute('''UPDATE denuncias SET totalComentarios = totalComentarios + 1 WHERE id=?''', (denuncia_id,))
    cur.close()
    return {}, 201


def delete_comentario(denuncia_id, args):
    cur = get_db().cursor()
    cur.execute('DELETE FROM comentarios WHERE id=?', (args.id,))
    cur.execute('''UPDATE denuncias SET totalComentarios = totalComentarios - 1 WHERE id=?''', (denuncia_id,))
    cur.close()
    return '', 201


def post_apoyo(denuncia_id, args):
    cur = get_db().cursor()
    cur.execute('''INSERT INTO apoyo (idUsuario, idDenuncia) values(?,?)''', (args.idUsuario, denuncia_id))
    cur.execute('''UPDATE denuncias SET apoyos = apoyos + 1 WHERE id=?''', (denuncia_id,))

    cur.close()
    return {}, 201


def delete_apoyo(denuncia_id, args):
    cur = get_db().cursor()
    cur.execute('''DELETE FROM apoyo WHERE idUsuario=? AND idDenuncia=?''', (args["Auth-Token"], denuncia_id))
    cur.execute('''UPDATE denuncias SET apoyos = apoyos -1 WHERE id=?''', (denuncia_id,))
    cur.close()
    return {}, 200
    

def post_reportar(denuncia_id, args):
    cur = get_db().cursor()
    cur.execute('''INSERT INTO reporte (idUsuario, idDenuncia) values(?,?)''', (args.idUsuario, denuncia_id))
    cur.execute('''UPDATE denuncias SET totalReportes = totalReportes +1 WHERE id=?''', (denuncia_id,))
    cur.close()
    return {}, 201
 

def get_usuarioapoyos(usuario_id):
    cur = get_db().cursor()
    all_apoyos_usuario = cur.execute('''SELECT c.id as idDenuncia, c.fecha, c.titulo, c.descripcion, c.imagenSmall as imagen, c.apoyos, c.totalComentarios, c.visualizaciones 
                                        FROM denuncias c 
                                        LEFT JOIN apoyo p ON p.idDenuncia = c.id 
                                        WHERE p.idUsuario = ?
                                        ORDER BY c.id DESC''',([usuario_id])).fetchall()
    cur.close()
    return [dict(d) for d in all_apoyos_usuario]


def get_usuarioreportadas(usuario_id): 
    cur = get_db().cursor()
    all_reportes_usuario = cur.execute('''SELECT c.id as idDenuncia, c.fecha, c.titulo, c.descripcion, c.imagenSmall as imagen, c.apoyos, c.totalComentarios, c.visualizaciones 
                                        FROM denuncias c 
                                        LEFT JOIN reporte p ON p.idDenuncia = c.id 
                                        WHERE p.idUsuario = ?
                                        ORDER BY c.id DESC''',([usuario_id])).fetchall()
    cur.close()
    return [dict(d) for d in all_reportes_usuario]



"""
When someone resets the database this function will be called upon. 
It's used to add defaultvalues into the database for testing.
"""
def denuncia_table():
    with app.app_context():
        create_denuncia_table()
        create_comentario_table()
        create_usuario_table()
        create_apoyo_table()
        create_reporte_table()
        create_administrador_table()

        add_denuncia(**DENUNCIAS[0])
        add_denuncia(**DENUNCIAS[1])
        add_denuncia(**DENUNCIAS[2])
        add_denuncia(**DENUNCIAS[3])
        add_denuncia(**DENUNCIAS[4])
        add_comentario(**COMENTARIOS[0])
        add_comentario(**COMENTARIOS[1])
        add_comentario(**COMENTARIOS[2])
        add_comentario(**COMENTARIOS[3])
        add_usuario(**USUARIOS[0])
        add_usuario(**USUARIOS[1])
        add_apoyo(**APOYOS[0])
        add_apoyo(**APOYOS[1])
        add_reporte(**REPORTES[0])
        add_reporte(**REPORTES[1])
        get_db().commit()


