import web
import config as config


class Insert:
    def __init__(self):
        pass

    def GET(self):  
        return config.render.insert() # renderiza la pagina insert.html
    
    def POST(self):
        formulario = web.input() # almacena los datos del formulario
        nombre = formulario['nombre'] # almacena el nombre escrito en el input
        num_cel = formulario['num_cel'] # almacena el contenido escrito en el input
        correo_electronico = formulario['correo_electronico'] # alamcena la cadena escrita en el input
        sexo = formulario['sexo'] # alamcena la cadena escrita en el input
        config.model_clientes.insert_clientes(nombre, ape_pat, ape_mat, colonia) # llama al metodo insert_clientes y le paso los datos guardados
        raise web.seeother('/clientes') # redirecciona al index.html
