#Referenciamos Flask
from flask import Flask, render_template

app= Flask(__name__) 

#Rutas de paginas
@app.route("/")
def index():
    nombre="filemona"
    lista1=["Español","Ingles","Frances"]
    return render_template("index.html", nombre=nombre, lista1=lista1) #Asi se pasan los parametros

@app.route("/usuarios")
def usuarios():
    return render_template("archivo2.html") #visualiza el archivo2.html



if __name__=="__main__":
    app.run( debug=True) #debug=True para que se actualice automaticamente