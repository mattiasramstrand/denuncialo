"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from FlaskWebProject import app
from flask_restful import reqparse, abort, Api, Resource
from api import *
from sql import * 


@app.after_request
def after_request(response):
    get_db().commit()
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization, Auth-Token')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/listaDenuncias')
def listaDenuncias():
    """Renders listaDenuncias."""
    return render_template(
        'listaDenuncias.html',
        title ='Panel principal de gestion de denuncias',
        create_comentario_table='Lista de denuncias',
        year=datetime.now().year,
        message='Listado de denuncias de la página.',
        lista = get_denuncialist()
        )

@app.route('/duplicadas')
@app.route('/duplicadas/<int:id>')
def listaDuplicadas(id):
    """Renders duplicadas."""
    lista_denuncias = get_denuncialist()
    denuncia = None
    for d in lista_denuncias:
        if(d['idDenuncia']==id): 
            denuncia = d
    return render_template(
        'listaDuplicadas.html',
        title ='Denuncias duplicadas',
        create_comentario_table='Lista de denuncias duplicadas',
        year=datetime.now().year,
        message='Listado de denuncias repetidas de la página.',
        lista = get_listaduplicados(lista_denuncias,denuncia)
        )

@app.route('/resetdb')
def resetdb():
    cur = get_db().cursor()
    cur.execute('DROP TABLE IF EXISTS denuncias')
    cur.execute('DROP TABLE IF EXISTS comentarios')
    cur.execute('DROP TABLE IF EXISTS apoyo')
    cur.execute('DROP TABLE IF EXISTS reporte')
    cur.execute('DROP TABLE IF EXISTS administrador')
    cur.execute('DROP TABLE IF EXISTS usuario')
    cur.close()
    denuncia_table()
    return 'reset ok'

















