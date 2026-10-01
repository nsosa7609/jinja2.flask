from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/tareas")
def tareas():
    lista_tareas = [
        "Crear una base de datos",
        "Crear un Back-End",
        "Conectar Front-End"
    ]

    return render_template("tareas.html", tareas=lista_tareas)

@app.route("/usuarios")
def usuarios():
    lista_usuarios = [
        {
            "nombre": "Naiomi",
            "correo": "naiomi@example.com"
        },
          {
            "nombre": "Michael",
            "correo": "michael@example.com"
        }
    ]

    return render_template("usuarios.html", usuarios=lista_usuarios)

if __name__ == "__main__":
    app.run(debug=True) 