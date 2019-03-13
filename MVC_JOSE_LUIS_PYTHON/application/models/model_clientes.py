import config as config # importa el archivo config

db = config.db # crea un objeto db del objeto db creado en config


#Metodo para seleccionar todos los registros de la tabla clientes

def select_clientes():
    try:
        return db.select('clientes') # Selecciona todos los registros de la tabla clientes
    except Exception as e:
        print "Model select_clientes Error {}".format(e.args)
        print "Model select_clientes Message {}".format(e.message)
        return None


#Metodo para seleccionar un registro que coincida con el nombre dado

def select_nombre(nombre):
    try:
        return db.select('clientes',where='nombre=$nombre', vars=locals())[0] # selecciona el primer registro que coincida con el nombre
    except Exception as e:
        print "Model select_nombre Error {}".format(e.args)
        print "Model select_nombre Message {}".format(e.message)
        return None


#Metodo para insertar un nuevo registro 

def insert_clientes(nombre,num_cel,correo_electronico,sexo):
    try:
        return db.insert('clientes', 
        nombre=nombre,
        num_cel=num_cel,
        correo_electronico=correo_electronico,
        sexo=sexo) # inserta un registro en producto
    except Exception as e:
        print "Model insert_clientes Error {}".format(e.args)
        print "Model insert_clientes Message {}".format(e.message)
        return None


#Metodo para eliminar un registro que coincida con el nombre recibido

def delete_clientes(nombre):
    try:
        return db.delete('clientes', where='nombre=$nombre',vars=locals()) # borra un registro de clientes
    except Exception as e:
        print "Model delete_clientes Error {}".format(e.args)
        print "Model delete_clientes Message {}".format(e.message)
        return None


#Metodo para actualizar los datos, del nombre recibido

def update_clientes(nombre,num_cel,correo_electronico,sexo): # actualiza los datos de la tabla clientes que coincidan con el nombre
    try:
        return db.update('clientes',
            num_cel=num_cel,
            correo_electronico=correo_electronico,
            sexo=sexo, 
            where='nombre=$nombre',
            vars=locals())
    except Exception as e:
        print "Model update_clientes Error {}".format(e.args)
        print "Model update_clientes Message {}".format(e.message)
        return None
