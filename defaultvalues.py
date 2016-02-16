"""
Default denuncias and comentarios.
 
"""



DENUNCIAS = [
    { #http://codigospostales.dices.net/codigospostales.php Codigos postales
        'id' : '0',
        'idUsuario' : 'uuid-test-movil',
        'fecha': '2015-05-21 11:04:13',
        'titulo': 'Fuente Rota',
        'descripcion': 'Que arreglen la fuente de una vez!',
        'categoria' : 'Mobiliario',
        'imagenSmall' : 'http://denuncialo.azurewebsites.net/static/denuncias_img/FuenteRota.jpg',
        'imagenBig' : 'http://denuncialo.azurewebsites.net/static/denuncias_img/FuenteRota.jpg',
        'latitud' : '39.483096',
        'longitud' : '-0.365877',
        'codigoPostal' : '46010',
        'direccion' : 'Calle de Jaca',
        'apoyos': '0',
    	'visualizaciones': '5',
        'totalComentarios': '1',
        'totalReportes': '0',
        'fechaModificacion': '2015-05-21 11:04:13',
		'estado': 'Publicada'
	},
	{
		'id' : '1',
		'idUsuario' : 'randomrandom',
		'fecha': '2015-03-24 13:04:23',
		'titulo': 'Calle en mal estado',
		'descripcion': 'Solo se puede pasar aqui en burro.',
		'categoria' : 'Mantenimiento',        
		'imagenSmall' : 'http://denuncialo.azurewebsites.net/static/denuncias_img/CalleMalEstado.jpg',
		'imagenBig' : 'http://denuncialo.azurewebsites.net/static/denuncias_img/CalleMalEstado.jpg',
		'latitud' : '39.483096',
		'longitud' : '-0.365877',
		'codigoPostal' : '46010',
		'direccion' : 'Calle de Jaca',
		'apoyos': '1',
		'visualizaciones': '50',
		'totalComentarios': '2',
		'totalReportes': '0',
		'fechaModificacion': '2015-05-21 11:04:13',
		'estado': 'Publicada'
	},
	{
		'id' : '2',
		'idUsuario' : 'randomrandom',
		'fecha': '2015-05-20 16:04:23',
		'titulo': 'Parque sucio',
		'descripcion': 'Esto es una cochinada.',
		'categoria' : 'Building',         
		'fecha': '2015-05-20 16:04:23',
		'titulo': 'Parque sucio',
		'descripcion': 'Esto es una cochinada.',
		'categoria' : 'Medioambiente',
		'imagenSmall' : 'http://denuncialo.azurewebsites.net/static/denuncias_img/ParqueSucio.jpg',        
		'imagenBig' : 'http://denuncialo.azurewebsites.net/static/denuncias_img/ParqueSucio.jpg',
		'latitud' : '39.475414',
		'longitud' : '-0.367823',
		'codigoPostal' : '46010',
		'direccion' : 'Paseo de la Albereda',
		'apoyos': '1',
		'visualizaciones': '3',
		'totalComentarios': '1',
		'totalReportes': '0',
		'fechaModificacion': '2015-05-21 11:04:13',
		'estado': 'Publicada'
    }, 
 
    {
		'id' : '3',
		'idUsuario' : 'randomrandom',
		'fecha': '2015-10-10 13:05:47',
		'titulo': 'Farola destrozada',
		'descripcion': 'La farola de la calle Padre Vina, esta derribada.',
		'categoria' : 'Mobiliario',
		'imagenSmall' : 'http://denuncialo.azurewebsites.net/static/denuncias_img/FarolaRota.jpg',        
		'imagenBig' : 'http://denuncialo.azurewebsites.net/static/denuncias_img/FarolaRota.jpg',
		'latitud' : '39.467909',
		'longitud' : '-0.362410',
		'codigoPostal' : '46004',
		'direccion' : 'Puente de Aragon',
		'apoyos': '0',
		'visualizaciones': '6',
		'totalComentarios': '0',
		'totalReportes': '1',
		'fechaModificacion': '2015-05-21 11:04:13',
		'estado': 'Publicada'
	},
	{ #No borrar, denuncia duplicadas para poder aplicar el filtro
		'id' : '4',
		'idUsuario' : 'randomrandom',
		'fecha': '2015-05-21 11:04:13',
		'titulo': 'Fuente destrozada',
		'descripcion': 'Que arreglen la fuente de una vez, porfavor!!!',
		'categoria' : 'Mobiliario',
		'imagenSmall' : 'http://denuncialo.azurewebsites.net/static/denuncias_img/FuenteRota.jpg',
		'imagenBig' : 'http://denuncialo.azurewebsites.net/static/denuncias_img/FuenteRota.jpg',
		'latitud' : '39.483096',
		'longitud' : '-0.365877',
		'codigoPostal' : '46010',
		'direccion' : 'Calle de Jaca',
		'apoyos': '0',
		'visualizaciones': '1',
		'totalComentarios': '0',
		'totalReportes': '1',
		'fechaModificacion': '2015-05-21 20:04:13',
		'estado': 'Publicada'
	}
]
 
COMENTARIOS = [
        {
        'id' : '1',
        'idDenuncia' : '1',
        'idUsuario' : 'uuid-test-movil',
		'fecha': '2015-05-21 17:04:13',
		'mensaje': 'Esto no puede ser'
	},
	{
        'id' : '2',
        'idDenuncia' : '0',
        'idUsuario' : 'randomrandom',
		'fecha': '2015-05-21 13:04:13',
        #idUsuario=0 soy yo, par poder modificar
		'mensaje': 'Que vengan a repararlo'
	},
	{
        'id' : '3',
        'idDenuncia' : '2',
        'idUsuario' : 'randomrandom',
		'fecha': '2015-05-21 20:04:13',
		'mensaje': 'Que pena me da que este esto asi',
	},
	{
        'id' : '4',
        'idDenuncia' : '1',
        'idUsuario' : 'randomrandom',
		'fecha': '2015-05-21 20:04:13',
		'mensaje': 'Casi pierdo una rueda del coche por esto',
	}
]


USUARIOS = [
	{
        'idUsuario' : 'uuid-test-movil',
        'telefono':'+34652452214',
        'imagenAvatar':'http://denuncialo.azurewebsites.net/static/usuario_img/logo.jpg',
		'nombre':'Mattias', 
		'email':'tester@inf.upv.es',
        'notificacionesGeneral' : '0',
        'notificacionesEstado' : '0',
        'notificacionesComentarios' : '0'

	},
	{
        'idUsuario' : 'anotherUser',
        'telefono':'+34 XXX XX XX XX',
        'imagenAvatar':'https://pbs.twimg.com/profile_images/425380665685999616/G7iwnZsN_normal.jpeg',
		'nombre':'Nicolas', 
		'email':'tester@inf.upv.es',
        'notificacionesGeneral' : '0',
        'notificacionesEstado' : '0',
        'notificacionesComentarios' : '0'
	}

]


APOYOS = [
	{
		'idApoyo' : '0',
        'idDenuncia': '1',
        'idUsuario': 'uuid-test-movil'

	},
	{
		'idApoyo' : '1',
        'idDenuncia': '2',
        'idUsuario':'randomrandom'
	}

]

REPORTES = [
	{
	    'idReporte' : '1',
	    'idDenuncia' : '3',
	    'idUsuario' : 'uuid-test-movil'
	},
	{
	    'idReporte' : '2',
	    'idDenuncia' : '4',
	    'idUsuario' : 'randomrandom'
	}

]
