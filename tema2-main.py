#Referenciamos Flask
from flask import Flask

app= Flask(__name__) 

#Rutas de paginas
@app.route("/")
def index():
    return "<h1>Hola mundo INDEX!</h1> --cambio 2" #Aqui todas las funciones deben regresar algo

@app.route("/hola")
def hola():
    return "<h1>Hola desde otra ruta!</h1> --ruta 2" 

@app.route("/nueva")
def nueva():
    return "<h1>Adios mundo cruel!</h1> --ruta 3"

if __name__=="__main__":
    app.run( debug=True) #debug=True para que se actualice automaticamente