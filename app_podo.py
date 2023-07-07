from flask import Flask, jsonify, request # del modulo flask importar la clase Flask y los métodos jsonify, request
from flask_cors import CORS # del modulo flask_cors importar CORS
from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow 
app = Flask(__name__)  # crear el objeto app de la clase Flask
CORS(app) # modulo cors es para que me permita acceder desde el frontend al backend

# configuro la base de datos, con el nombre, el usuario y la clave 
#app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:9669@localhost/proyecto' # servidor backend local
# para un servidor backend remoto en pythonanywhere
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://jnrosas:passwordmysql@jnrosas.mysql.pythonanywhere-services.com/jnrosas$local'
# URI de la BBDD driver de la BD user:clave@URLBBDD/nombreBBDD
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False #none 
#crea el objeto db de la clase SQLAlquemy 
db= SQLAlchemy(app) 
#crea el objeto ma de de la clase Marshmallow
ma=Marshmallow(app) 

from controladores import *


# programa principal ******************************* 
if __name__=='__main__': 
  app.run(debug=True, port=5000) # ejecuta el servidor Flask en el puerto 5000
  