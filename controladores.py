from flask import Flask, jsonify, request # del modulo flask importar la clase Flask y los métodos jsonify, request
from app_podo import app, ma
from modelos import *

class ClientSchema(ma.Schema): 
  class Meta: 
    fields=('id','name','lastname','dob','dni','phone','insurance','photo')
    
client_schema=ClientSchema() # El objeto client_schema es para traer un cliente 
clients_schema=ClientSchema(many=True) # El objeto clients_schema es para traer multiples registros de clientes

# crea los endpoint o rutas (json)
@app.route('/clients', methods=['GET']) 
def get_Clients(): 
  all_clients=Client.query.all() # el metodo query.all() lo hereda de db.Model
  result=clients_schema.dump(all_clients) # el metodo dump() lo hereda de ma.schema y trae todos los registros de la tabla
  return jsonify(result) # retorna un JSON de todos los registros de la tabla

@app.route('/clients/<id>', methods=['GET']) 
def get_client(id): 
  client=Client.query.get(id) 
  return client_schema.jsonify(client) # retorna el JSON de un cliente recibido como parametro

@app.route('/clients/<id>', methods=['DELETE']) 
def delete_client(id): 
  client=Client.query.get(id) 
  db.session.delete(client) 
  db.session.commit() 
  return client_schema.jsonify(client) # me devuelve un json con el registro eliminado
  
@app.route('/clients', methods=['POST']) # crea ruta o endpoint 
def create_client(): 
  #print(request.json) # request.json contiene el json que envio el cliente 
  name=request.json['name'] 
  lastname=request.json['lastname'] 
  dob=request.json['dob'] 
  dni=request.json['dni'] 
  phone=request.json['phone'] 
  insurance=request.json['insurance']
  photo=request.json['photo'] 
  new_client=Client(name,lastname,dob,dni,phone,insurance,photo) 
  db.session.add(new_client) 
  db.session.commit() 
  return client_schema.jsonify(new_client)
  
@app.route('/clients/<id>', methods=['PUT']) 
def update_client(id): 
  client=Client.query.get(id)
  client.name=request.json['name'] 
  client.lastname=request.json['lastname'] 
  client.dob=request.json['dob'] 
  client.dni=request.json['dni']
  client.phone=request.json['phone'] 
  client.insurance=request.json['insurance']
  client.photo=request.json['photo']
  db.session.commit() 
  return client_schema.jsonify(client)
