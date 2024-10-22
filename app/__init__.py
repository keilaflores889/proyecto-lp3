from flask import Flask

app = Flask(__name__)

# importar referenciales
from app.rutas.referenciales.ciudad.ciudad_routes import ciumod #ciudad
from app.rutas.referenciales.paises.pais_routes import paimod   #pais
from app.rutas.referenciales.nacionalidad.nacionalidad_routes import naciomod  #nacionalidad
from app.rutas.referenciales.ocupacion.ocupacion_routes import ocupmod  #ocupacion
from app.rutas.referenciales.estado_civil.estado_civil_routes import estacivmod  #estado civil
from app.rutas.referenciales.sexo.sexo_routes import sexmod  #sexo
from app.rutas.referenciales.estado_cita.estado_cita_routes import estacitmod  #estado de la cita
from app.rutas.referenciales.persona.persona_routes import persmod  #persona
from app.rutas.referenciales.especialidad.especialidad_routes import especimod  #especialidad
from app.rutas.referenciales.dia.dia_routes import diamod  #dia
from app.rutas.referenciales.duracion_consulta.duracion_consulta_routes import duraconsumod  #duracion de la consulta
from app.rutas.referenciales.instrumento.instrumento_routes import instmod  #instrumento utilizado
from app.rutas.referenciales.turno.turno_routes import turmod  #turno
from app.rutas.referenciales.tratamiento.tratamiento_routes import tratmod  #tratamiento
from app.rutas.referenciales.diagnostico.diagnostico_routes import diagmod  #diagnostico

# importar gestionar compras
from app.rutas.gestionar_compras.registrar_pedido_compras.registrar_pedidos_compras_routes \
    import pdcmod


# registrar referenciales
modulo0 = '/referenciales'
app.register_blueprint(ciumod, url_prefix=f'{modulo0}/ciudad') #ciudad
app.register_blueprint(paimod, url_prefix=f'{modulo0}/paises') #pais
app.register_blueprint(naciomod, url_prefix=f'{modulo0}/nacionalidad')  #nacionalidad
app.register_blueprint(ocupmod, url_prefix=f'{modulo0}/ocupacion')  #ocupacion
app.register_blueprint(estacivmod, url_prefix=f'{modulo0}/estadocivil')  #estado civil
app.register_blueprint(sexmod, url_prefix=f'{modulo0}/sexo')  #sexo
app.register_blueprint(estacitmod, url_prefix=f'{modulo0}/estadocita')  #estado de la cita
app.register_blueprint(persmod, url_prefix=f'{modulo0}/persona') #persona
app.register_blueprint(especimod, url_prefix=f'{modulo0}/especialidad') #especialidad
app.register_blueprint(diamod, url_prefix=f'{modulo0}/dia') #dia
app.register_blueprint(duraconsumod, url_prefix=f'{modulo0}/duracionconsulta') #duracion de la consulta
app.register_blueprint(instmod, url_prefix=f'{modulo0}/instrumento') #instrumento utilizado
app.register_blueprint(turmod, url_prefix=f'{modulo0}/turno') #turno
app.register_blueprint(tratmod, url_prefix=f'{modulo0}/tratamiento') #tratamiento
app.register_blueprint(diagmod, url_prefix=f'{modulo0}/diagnostico') #diagnostico

# registro de modulos - gestionar compras
modulo1 = '/gestionar-compras'
app.register_blueprint(pdcmod, url_prefix=f'{modulo1}/registrar-pedido-compras')


#ciudad
from app.rutas.referenciales.ciudad.ciudad_api import ciuapi

#pais
from app.rutas.referenciales.paises.pais_api import paisapi

#nacionalidad
from app.rutas.referenciales.nacionalidad.nacionalidad_api import nacioapi

#nacionalidad
from app.rutas.referenciales.ocupacion.ocupacion_api import ocupapi

#estado civil
from app.rutas.referenciales.estado_civil.estado_civil_api import estacivapi

#sexo
from app.rutas.referenciales.sexo.sexo_api import sexapi

#estado de la cita
from app.rutas.referenciales.estado_cita.estado_cita_api import estacitapi

#persona
from app.rutas.referenciales.persona.persona_api import persapi

#especialidad
from app.rutas.referenciales.especialidad.especialidad_api import especiapi

#dia
from app.rutas.referenciales.dia.dia_api import diaapi

#duracion de la consulta
from app.rutas.referenciales.duracion_consulta.duracion_consulta_api import duraconsuapi

#instrumento utilizado
from app.rutas.referenciales.instrumento.instrumento_api import instapi

#turno
from app.rutas.referenciales.turno.turno_api import turnoapi

#tratamiento
from app.rutas.referenciales.tratamiento.tratamiento_api import tratapi

#diagnostico
from app.rutas.referenciales.diagnostico.diagnostico_api import diagapi

#pedido de compra
from app.rutas.gestionar_compras.registrar_pedido_compras.registrar_pedido_compras_api \
    import pdcapi


# APIS v1
#Ciudad
apiversion1 = '/api/v1'
app.register_blueprint(ciuapi, url_prefix=apiversion1)

#Pais
apiversion1 = '/api/v1'
app.register_blueprint(paisapi, url_prefix=apiversion1)

#nacionalidad
apiversion1 = '/api/v1'
app.register_blueprint(nacioapi, url_prefix=apiversion1)

#ocupacion
apiversion1 = '/api/v1'
app.register_blueprint(ocupapi, url_prefix=apiversion1)

#Estado civil
apiversion1 = '/api/v1'
app.register_blueprint(estacivapi, url_prefix=apiversion1)

#sexo
apiversion1 = '/api/v1'
app.register_blueprint(sexapi, url_prefix=apiversion1)

#Estado de la cita
apiversion1 = '/api/v1'
app.register_blueprint(estacitapi, url_prefix=apiversion1)

#persona
apiversion1 = '/api/v1'
app.register_blueprint(persapi, url_prefix=apiversion1)

#especialidad
apiversion1 = '/api/v1'
app.register_blueprint(especiapi, url_prefix=apiversion1)

#dia
apiversion1 = '/api/v1'
app.register_blueprint(diaapi, url_prefix=apiversion1)

#duracion de la consulta
apiversion1 = '/api/v1'
app.register_blueprint(duraconsuapi, url_prefix=apiversion1)

#instrumento utilizado
apiversion1 = '/api/v1'
app.register_blueprint(instapi, url_prefix=apiversion1)

#turno
apiversion1 = '/api/v1'
app.register_blueprint(turnoapi, url_prefix=apiversion1)

#tratamiento
apiversion1 = '/api/v1'
app.register_blueprint(tratapi, url_prefix=apiversion1)

#diagnostico
apiversion1 = '/api/v1'
app.register_blueprint(diagapi, url_prefix=apiversion1)


# Gestionar compras API
apiversion1 = '/api/v1'
app.register_blueprint(pdcapi, url_prefix=f'{apiversion1}/{modulo1}/registrar-pedido-compras')