#Referenciamos Flask
from flask import Flask

app= Flask(__name__) 

#Rutas de paginas
@app.route("/user/<string:username>") #<username> es un parametro
def user(username):
    return "<h1>Hola! "+username+"</h1> Mandar parametros" #Aqui todas las funciones deben regresar algo

@app.route("/numero/<int:num>")
def numero(num):
    return "<h1> Este es el numero: {} ".format(num)+"</h1>"


@app.route("/user/<int:id>/<string:name>")
def func(id, nombre):
    return "<h1> ID {} Nombre".format(id,nombre)+"</h1>"

@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1, n2):
    return "<h1> Numero 1: {} Numero 2: ".format(n1,n2)+"</h1>"+"<h2> La suma es: {}".format(n1+n2)+"</h2>"



if __name__=="__main__":
    app.run( debug=True) #debug=True para que se actualice automaticamente