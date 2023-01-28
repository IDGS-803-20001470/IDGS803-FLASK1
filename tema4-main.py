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
        return "<h1>la suma es: {}".format(str(int(num1)+int(num2)))+"</h1>"

    else:
         return """
         <form action="/operasBas" method="POST">
         <label>Numero 1</label>
         <input type="text" name="num1"></input>
         </br></br>
         <label>Numero 2</label>
         <input type="text" name="num2"></input>
         <input type="submit" value="calcular">Enviar numeros</input>
         </form>
        
         """
        
    




if __name__=="__main__":
    app.run( debug=True) #debug=True para que se actualice automaticamente