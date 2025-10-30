from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'clave_secreta'


def calcular_calorias(grasas, proteinas, carbohidratos):
    return {
        'Grasas': grasas * 9,
        'Proteínas': proteinas * 4,
        'Carbohidratos': carbohidratos * 4
    }


def clasificar(calorias):
    mayor = max(calorias, key=calorias.get)
    return f'Fuente de {mayor}'


@app.route('/clasificar_macro', methods=['GET', 'POST'])
def clasificar_macro():
    if 'alimentos_clasificados' not in session:
        session['alimentos_clasificados'] = []

    if request.method == 'POST':
        nombre = request.form.get('nombre')
        grasas = float(request.form.get('grasas', 0))
        proteinas = float(request.form.get('proteinas', 0))
        carbohidratos = float(request.form.get('carbohidratos', 0))

        calorias = calcular_calorias(grasas, proteinas, carbohidratos)
        resultado = clasificar(calorias)

        nuevos = session['alimentos_clasificados']
        nuevos.append({'nombre': nombre, 'clasificacion': resultado})
        session['alimentos_clasificados'] = nuevos
        session.modified = True

        return redirect('/clasificar_macro')

    return render_template('clasificar_macro.html', alimentos=session.get('alimentos_clasificados', []))


@app.route('/limpiar_lista', methods=['POST'])
def limpiar_lista():
    session['alimentos_clasificados'] = []
    session.modified = True
    return redirect('/clasificar_macro')

if __name__ == '__main__':
    app.run(debug=True)