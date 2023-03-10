from flask import Flask, render_template
from flask import request
import forms 

app = Flask(__name__)

@app.route("/formulario")
def formulario():
    return render_template("formulario.html")

@app.route("/Alumnos", methods=['GET', 'POST'])
def alumnos():
    print("ALUMNO COMPLETO", request.form)
    alum_form= forms.UserForm(request.form) # Aqui se crea el objeto de la clase UserForm
    if request.method == 'POST':
        print(alum_form.matricula.data)
        print(alum_form.nombre.data)

    return render_template("Alumnos.html", form=alum_form)

if __name__ == "__main__":
    app.run(debug=True)