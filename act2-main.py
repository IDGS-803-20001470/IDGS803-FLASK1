
#Referenciamos Flask
from flask import Flask, render_template
from flask import request
import  claseAct2 as objClase

app= Flask(__name__) 

#Rutas de paginas
#Rutas de paginas
@app.route("/")
def index():
    nombre="RICARDO REYNA MARTINEZ"
    lista1=["Español","Ingles","Frances"]
    return render_template("index.html", nombre=nombre, lista1=lista1) #Asi se pasan los parametros
@app.route("/resultado", methods=["POST"])
def resultado():
    n1= request.form.get("txtNum1")
    n2= request.form.get("txtNum2")
    res=int(n1)*int(n2)
    return render_template("resultado.html", n1=n1, n2=n2, res=res) #visualiza el resultado.html

@app.route("/cinepolis")
def cinepolis():
    return render_template("cinepolis.html") 


@app.route("/cinepoliserror",  methods=["POST"])
def cinepoliserror():
    return render_template("cinepoliserror.html") 

@app.route("/salida",  methods=["POST", "GET"])
def salida():
    return render_template("salida.html") 



@app.route("/cinepolisR", methods=["POST"])
def cinepolisR():
    nombre= request.form.get("txtNombre")
    cantCompradores= int(request.form.get("txtCantC"))
    tarjetaC= request.form.get("opcion")
    cantBoletos = int(request.form.get("txtCantB"))
    ob=objClase.operaciones()



    veri=ob.verificarMaximoBoletos(cantCompradores, cantBoletos)
    if(veri==True):
        return render_template("cinepoliserror.html") 
    else:
        res1= ob.verificarDescuento(cantBoletos)
        print("OPCION1", tarjetaC)
        res2= ob.verificarTarjeta(tarjetaC, res1)
        return render_template("cinepolisR.html",res=res2, nombre=nombre) 
         

    
        

            
        
    

if __name__=="__main__":
    app.run( debug=True) #debug=True para que se actualice automaticamente