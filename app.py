from flask import Flask

app = Flask(__name__)

@app.route('/')
def hola_flask():
    return "<h1>¡Hola, Flask!</h1><hr>"

@app.route('/ruta2')
def ruta2():
    return "<strong>Estamos en la segunda ruta</strong>"

@app.route('/ruta3')
def ruta3():
    return "<em>Estamos en la tercera ruta</em><hr>"

@app.route('/notas')
@app.route('/notas/<float:nota1>/<float:nota2>/<float:nota3>')
def notas(nota1=0, nota2=0, nota3=0):
    resultado = (nota1 * 30) / 100 + (nota2 * 30) / 100 + (nota3 * 40) / 100
    return f"<h1>Tu resultado es: {resultado}</h1><hr>"

@app.route('/edades')
@app.route('/edades/<int:edad>')
def edades(edad=0):
    if edad < 18:
        R = "Eres menor de edad"
    elif edad < 60:
        R = "Eres adulto"
    else:
        R = "Eres adulto mayor"
    return f"<h1>La persona es: {R}</h1><hr>"

if __name__ == "__main__": 
    app.run(debug=True)
