#Referenciamos Flask
from flask import Flask

#Referenciamos request para peticion http
from flask import request 

app= Flask(__name__) 

#Rutas de paginas
@app.route("/operasBas", methods=["POST", "GET"]) # En methods ponemos que metodo vamos a utilizar, ya sea Get o POST o los dos
def operasBas():
    if request.method=="POST":
        num1=request.form.get("num1")
        num2=request.form.get("num2")
       
        opcion=request.form.get("opcion")
       
        if(opcion=="suma"):
            return "<h1>la suma es: {}".format(str(int(num1)+int(num2)))+"</h1>"
        elif(opcion=="resta"):
            return "<h1>la resta es: {}".format(str(int(num1)-int(num2)))+"</h1>"
        elif(opcion=="multi"):
            return "<h1>la Multi es: {}".format(str(int(num1)*int(num2)))+"</h1>"
        else:
            return "<h1>la division es: {}".format(str(int(num1)/int(num2)))+"</h1>"

    else:
         return """
         <form action="/operasBas" method="POST">
         <label>Numero 1</label>
         <input type="text" name="num1"></input>
         </br></br>
         <label>Numero 2</label>
         <input type="text" name="num2"></input>
         </br></br>
         <input type="radio" id="html1" name="opcion" value="suma">
         <label for="html">SUMA</label><br>
         <input type="radio" id="resta" name="opcion" value="resta">
         <label for="html">RESTA</label><br>
         <input type="radio" id="html2" name="opcion" value="multi">
         <label for="html">Multiplicacion</label><br>
         <input type="radio" id="html3" name="opcion" value="divi">
         <label for="html">Division</label><br>
         <input type="submit" value="calcular"></input>
         </form>
        
         """
        
    




if __name__=="__main__":
    app.run( debug=True) #debug=True para que se actualice automaticamente