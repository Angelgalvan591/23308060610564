from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'clave_secreta'

@app.route('/clasificar_macro', methods=['GET', 'POST'])
def clasificar_macro():
    if 'alimentos_clasificados' not in session:
        session['alimentos_clasificados'] = []

    if request.method == 'POST':
        nombre = request.form.get('nombre')
        grasas = float(request.form.get('grasas', 0))
        proteinas = float(request.form.get('proteinas', 0))
        carbohidratos = float(request.form.get('carbohidratos', 0))

        g_cal = grasas * 9
        p_cal = proteinas * 4
        c_cal = carbohidratos * 4
        total = g_cal + p_cal + c_cal

        tipo = max({'Grasas': g_cal, 'Proteínas': p_cal, 'Carbohidratos': c_cal}, key=lambda x: {'Grasas': g_cal, 'Proteínas': p_cal, 'Carbohidratos': c_cal}[x])
        resultado = f'Fuente de {tipo}'

        session['alimentos_clasificados'].append({'nombre': nombre, 'clasificacion': resultado})
        return redirect('/clasificar_macro')

    return render_template('clasificar_macro.html', alimentos=session['alimentos_clasificados'])

if __name__ == '__main__':
    app.run(debug=True)