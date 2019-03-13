import web
import config as config


class Update:
    def __init__(self):
        pass

    def GET(self, nombre): 
        clientes = config.model_clientes.select_nombre(nombre) # Selecciona el registro que coincida con nombre
        return config.render.update(clientes) # Envia el registro y renderiza update.html
    
    def POST(self,nombre):
        formulario = web.input()
        nombre = formulario['nombre'] 
        num_cel = formulario['num_cel'] 
        correo_electronico = formulario['correo_electronico'] 
        sexo = formulario['sexo'] 
        config.model_clientes.update_clientes(nombre, ape_pat, ape_mat, colonia)
        raise web.seeother('/clientes') 
