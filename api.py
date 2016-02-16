"""
Sets up the API functions.
"""

from datetime import datetime, timedelta
from flask import request, g, jsonify
from flask_restful import reqparse, abort, Api, Resource
from datetime import datetime, timedelta
from FlaskWebProject import app
from sql import *
from defaultvalues import *
import sqlite3, json
import base64



def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in TODOS:
        abort(404, message="Todo {} doesn't exist".format(todo_id))


parserDenuncialist = reqparse.RequestParser()
parserDenuncialist.add_argument('id')
parserDenuncialist.add_argument('idUsuario')
parserDenuncialist.add_argument('fecha')
parserDenuncialist.add_argument('titulo')
parserDenuncialist.add_argument('descripcion')
parserDenuncialist.add_argument('categoria')
parserDenuncialist.add_argument('imagen')
parserDenuncialist.add_argument('latitud')
parserDenuncialist.add_argument('longitud')
parserDenuncialist.add_argument('codigoPostal')
parserDenuncialist.add_argument('direccion')
parserDenuncialist.add_argument('apoyos')
parserDenuncialist.add_argument('visualizaciones')
parserDenuncialist.add_argument('totalComentarios')
parserDenuncialist.add_argument('totalReportes')
parserDenuncialist.add_argument('fechaModificacion')
parserDenuncialist.add_argument('estado')
parserDenuncialist.add_argument('Auth-Token', location='headers')
parserDenuncialist.add_argument('filter', location='args')
parserDenuncialist.add_argument('latitud', location='args')
parserDenuncialist.add_argument('longitud', location='args')

parserDenuncia = reqparse.RequestParser()
parserDenuncia.add_argument('id')
parserDenuncia.add_argument('idUsuario')
parserDenuncia.add_argument('fecha')
parserDenuncia.add_argument('titulo')
parserDenuncia.add_argument('descripcion')
parserDenuncia.add_argument('categoria')
parserDenuncia.add_argument('imagenSmall')
parserDenuncia.add_argument('imagenBig')
parserDenuncia.add_argument('latitud')
parserDenuncia.add_argument('longitud')
parserDenuncia.add_argument('direccion')
parserDenuncia.add_argument('codigoPostal')
parserDenuncia.add_argument('apoyos')
parserDenuncia.add_argument('visualizaciones')
parserDenuncia.add_argument('totalComentarios')
parserDenuncia.add_argument('totalReportes')
parserDenuncia.add_argument('fechaModificacion')
parserDenuncia.add_argument('estado')
parserDenuncia.add_argument('Auth-Token', location='headers')

parserComentario = reqparse.RequestParser()
parserComentario.add_argument('id')
parserComentario.add_argument('idDenuncia')
parserComentario.add_argument('idUsuario')
parserComentario.add_argument('fecha')
parserComentario.add_argument('mensaje')
parserComentario.add_argument('Auth-Token', location='headers')

parserUsuario = reqparse.RequestParser()
parserUsuario.add_argument('idUsuario')
parserUsuario.add_argument('telefono')
parserUsuario.add_argument('imagenAvatar')
parserUsuario.add_argument('nombre')
parserUsuario.add_argument('email')
parserUsuario.add_argument('notificacionesGeneral')
parserUsuario.add_argument('notificacionesEstado')
parserUsuario.add_argument('notificacionesComentarios')
parserUsuario.add_argument('Auth-Token', location='headers')

parserApoyo = reqparse.RequestParser()
parserApoyo.add_argument('idUsuario')
parserApoyo.add_argument('Auth-Token', location='headers')

parserReporte = reqparse.RequestParser()
parserReporte.add_argument('idUsuario')
parserReporte.add_argument('Auth-Token', location='headers')

parserAdministrador = reqparse.RequestParser()
parserAdministrador.add_argument('idAdmin')
parserAdministrador.add_argument('usuario')
parserAdministrador.add_argument('clave')
parserAdministrador.add_argument('email')
parserAdministrador.add_argument('Auth-Token', location='headers')



# Todo
# shows a single todo item and lets you delete a todo item
class Todo(Resource):
    def get(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        return TODOS[todo_id]

    def delete(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        del TODOS[todo_id]
        return '', 204

    def put(self, todo_id):
        args = parser.parse_args()
        task = {'task': args['task']}
        TODOS[todo_id] = task
        return task, 201

# TodoList
# shows a list of all todos, and lets you POST to add new tasks
class TodoList(Resource):
    def get(self):
        return TODOS

    def post(self):
        args = parser.parse_args()
        todo_id = int(max(TODOS.keys()).lstrip('todo')) + 1
        todo_id = 'todo%i' % todo_id
        TODOS[todo_id] = {'task': args['task']}
        return TODOS[todo_id], 201


class DenunciasList(Resource):
    def get(self):
        args = parserDenuncialist.parse_args()
        return get_denuncialist(args)

    def post(self):
        args = parserDenuncialist.parse_args()
        return post_denuncialist(args)


class Denuncia(Resource):
    def get(self, denuncia_id):
        args = parserDenuncia.parse_args()
        return get_denuncia(denuncia_id, args)

    def delete(self, denuncia_id):
        args = parserDenuncia.parse_args()
        return delete_denuncia(denuncia_id, args)

    def put(self, denuncia_id):
        args = parserDenuncia.parse_args()
        return put_denuncia(denuncia_id, args)


class ComentariosList(Resource):
    def get(self, denuncia_id):
        return get_comentariolist(denuncia_id)

    def post(self, denuncia_id):
        args = parserComentario.parse_args()
        return post_comentariolist(denuncia_id, args)


class Comentario(Resource):
    def put(self, denuncia_id):
        args = parserComentario.parse_args()
        return post_comentario(denuncia_id, args)

    def delete(self, denuncia_id):
        args = parserComentario.parse_args()
        return delete_comentario(denuncia_id, args)


class Apoyo(Resource):
    def post(self, denuncia_id):
        args = parserApoyo.parse_args()
        return post_apoyo(denuncia_id, args)

    def delete(self, denuncia_id):
        args = parserApoyo.parse_args()
        return delete_apoyo(denuncia_id, args)


class Reportar(Resource):
    def post(self, denuncia_id):
        args = parserReporte.parse_args()
        return post_reportar(denuncia_id, args)

class Usuario(Resource):
    def get(self, usuario_id):
        return get_usuario(usuario_id)

    def put(self, usuario_id):
        args = parserUsuario.parse_args()
        return put_usuario(usuario_id, args)

class UsuarioDenuncias(Resource):
    def get(self,usuario_id):
        return get_usuariodenuncias(usuario_id)

class UsuarioApoyos(Resource):
    def get(self, usuario_id):
        return get_usuarioapoyos(usuario_id)

class UsuarioReportadas(Resource):
    def get(self, usuario_id):
        return get_usuarioreportadas(usuario_id)

class UsuarioList(Resource):
    def get(self):
        return get_usuariolist()

class MailTo(Resource):
    def get(self):
        return testMail()


"""
Actually setup the Api resource routing here. 
Theese routes is the ones connected to the URL.
Each URL connects with functions from the back end.
"""

api = Api(app)

api.add_resource(TodoList, '/api/todos')
api.add_resource(Todo, '/api/todos/<todo_id>')
api.add_resource(DenunciasList, '/api/denuncias')
api.add_resource(Denuncia, '/api/denuncias/<denuncia_id>')
api.add_resource(Apoyo, '/api/denuncias/<denuncia_id>/apoyar')
api.add_resource(ComentariosList, '/api/denuncias/<denuncia_id>/comentarios')
api.add_resource(Comentario, '/api/denuncias/<denuncia_id>/comentarios/<comentario_id>')
api.add_resource(Reportar, '/api/denuncias/<denuncia_id>/reportar')
api.add_resource(Usuario, '/api/usuario/<usuario_id>')
api.add_resource(UsuarioDenuncias, '/api/usuario/<usuario_id>/denuncias')
api.add_resource(UsuarioApoyos, '/api/usuario/<usuario_id>/apoyos')
api.add_resource(UsuarioReportadas, '/api/usuario/<usuario_id>/reportadas')

## For debug use
api.add_resource(UsuarioList, '/api/usuario')
api.add_resource(MailTo, '/api/mail')