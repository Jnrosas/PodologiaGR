from app_podo import app, db

class Client(db.Model): # la clase Client hereda de db.Model 
  # define los campos de la tabla
  id=db.Column(db.Integer, primary_key=True) 
  name=db.Column(db.String(100))
  lastname=db.Column(db.String(100))
  dob=db.Column(db.Date) 
  dni=db.Column(db.String(100))
  phone=db.Column(db.String(100)) 
  insurance=db.Column(db.String(100))
  photo=db.Column(db.String(400)) 
  def __init__(self,name,lastname,dob,dni,phone,insurance,photo):  #crea el constructor de la clase
    self.name=name
    self.lastname=lastname 
    self.dob=dob 
    self.dni=dni
    self.phone=phone 
    self.insurance=insurance
    self.photo=photo

# si hay que crear mas tablas , se hace aqui
    
with app.app_context(): 
  db.create_all() # aqui crea todas las tablas
  
