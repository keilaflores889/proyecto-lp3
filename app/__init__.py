from flask import Flask

app = Flask(__name__)

# importar referenciales
from app.rutas.referenciales.ciudad.ciudad_routes import ciumod #ciudad
from app.rutas.referenciales.paises.pais_routes import paimod   #pais
from app.rutas.referenciales.correo.correo_routes import cormod #correo
from app.rutas.referenciales.direccion.direccion_routes import diremod #direccion
from app.rutas.referenciales.telefono.telefono_routes import telmod  #telefono
from app.rutas.referenciales.nacionalidad.nacionalidad_routes import naciomod  #nacionalidad
from app.rutas.referenciales.ocupacion.ocupacion_routes import ocupmod  #ocupacion
from app.rutas.referenciales.estado_civil.estado_civil_routes import estacivmod  #estado civil

# registrar referenciales
modulo0 = '/referenciales'
app.register_blueprint(ciumod, url_prefix=f'{modulo0}/ciudad') #ciudad
app.register_blueprint(paimod, url_prefix=f'{modulo0}/paises') #pais
app.register_blueprint(cormod, url_prefix=f'{modulo0}/correo') #correo
app.register_blueprint(diremod, url_prefix=f'{modulo0}/direccion') #direccion
app.register_blueprint(telmod, url_prefix=f'{modulo0}/direccion')  #telefono
app.register_blueprint(naciomod, url_prefix=f'{modulo0}/nacionalidad')  #nacionalidad
app.register_blueprint(ocupmod, url_prefix=f'{modulo0}/ocupacion')  #ocupacion
app.register_blueprint(estacivmod, url_prefix=f'{modulo0}/estadocivil')  #estado civil
 
#ciudad
from app.rutas.referenciales.ciudad.ciudad_api import ciuapi

#pais
from app.rutas.referenciales.paises.pais_api import paisapi

#coreo
from app.rutas.referenciales.correo.correo_api import correoapi

#direccion
from.rutas.referenciales.direccion.direccion_api import direapi

#telefono
from app.rutas.referenciales.telefono.telefono_api import telapi

#nacionalidad
from app.rutas.referenciales.nacionalidad.nacionalidad_api import nacioapi

#nacionalidad
from app.rutas.referenciales.ocupacion.ocupacion_api import ocupapi

#estado civil
from app.rutas.referenciales.estado_civil.estado_civil_api import estacivapi

# APIS v1
#Ciudad
version1 = '/api/v1'
app.register_blueprint(ciuapi, url_prefix=version1)

#Pais
version1 = '/api/v1'
app.register_blueprint(paisapi, url_prefix=version1)

#correo
version1 = '/api/v1'
app.register_blueprint(correoapi, url_prefix=version1)

#direccion
version1 = '/api/v1'
app.register_blueprint(direapi, url_prefix=version1)

#telefono
version1 = '/api/v1'
app.register_blueprint(telapi, url_prefix=version1)

#nacionalidad
version1 = '/api/v1'
app.register_blueprint(nacioapi, url_prefix=version1)

#ocupacion
version1 = '/api/v1'
app.register_blueprint(ocupapi, url_prefix=version1)

#ocupacion
version1 = '/api/v1'
app.register_blueprint(estacivapi, url_prefix=version1)