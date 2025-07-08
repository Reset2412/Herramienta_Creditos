from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
import os


# ─────────────────────────────────────────────────────────────
# CONFIGURACIÓN Y CREACIÓN DE LA APP
# ─────────────────────────────────────────────────────────────


# Configuración de la aplicación
app = Flask(__name__)
app.secret_key = 'JoshuaPaz' # Clave secreta para sesiones y mensajes flash

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(basedir, 'database', 'creditos.db')}"
db = SQLAlchemy(app)


# ─────────────────────────────────────────────────────────────
# MODELO DE BASE DE DATOS
# ─────────────────────────────────────────────────────────────


# Modelo de datos
class Credito(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cliente = db.Column(db.String(100), nullable=False)
    monto = db.Column(db.Float, nullable=False)
    tasa_interes = db.Column(db.Float, nullable=False)
    plazo = db.Column(db.Integer, nullable=False)
    fecha_otorgamiento = db.Column(db.Date, nullable=False)
    
    
# ─────────────────────────────────────────────────────────────
# RUTAS DE LA APLICACIÓN
# ─────────────────────────────────────────────────────────────


# Ruta principal
@app.route('/')
def home():
    """Página de inicio"""
    return render_template('index.html')

# Formulario para registrar crédito
@app.route('/registroCredito')
def registroCredito():
    """Formulario para registrar un nuevo crédito"""
    return render_template('registroCredito.html')

# Acción para guardar nuevo crédito
@app.route('/registro', methods=['POST'])
def registro():
    """Registra un nuevo crédito en la base de datos"""
    try:
        fecha_str = request.form['fecha_otorgamiento']
        fecha = datetime.strptime(fecha_str, "%Y-%m-%d").date()
        nuevo_credito = Credito(
            cliente=request.form['cliente'],
            monto=float(request.form['monto']),
            tasa_interes=float(request.form['tasa_interes']),
            plazo=int(request.form['plazo']),
            fecha_otorgamiento=fecha
        )
        db.session.add(nuevo_credito)
        db.session.commit()
        return redirect(url_for('creditos'))
    except Exception as e:
        db.session.rollback()
        return f"Error al registrar crédito: {e}", 500

# Listado de créditos
@app.route('/creditos')
def creditos():
    creditos = Credito.query.all()

    # Total monto por cliente
    total_por_cliente = (
        db.session.query(Credito.cliente, func.sum(Credito.monto))
        .group_by(Credito.cliente)
        .all()
    )
    clientes = [c[0] for c in total_por_cliente]
    montos = [float(c[1]) for c in total_por_cliente]

    # Conteo créditos por cliente
    conteo_por_cliente = (
        db.session.query(Credito.cliente, func.count(Credito.id))
        .group_by(Credito.cliente)
        .all()
    )
    conteos = [c[1] for c in conteo_por_cliente]

    return render_template(
        'listaCredito.html',
        creditos=creditos,
        clientes=clientes,
        montos=montos,
        conteos=conteos
    )

# Eliminar crédito por ID
@app.route('/eliminarCredito/<int:id>')
def eliminarCredito(id):
    """Elimina un crédito por ID"""
    credito = Credito.query.get_or_404(id)
    db.session.delete(credito)
    db.session.commit()
    return redirect(url_for('creditos'))

# Editar crédito por ID
@app.route('/editarCredito/<int:id>', methods=['GET', 'POST'])
def editarCredito(id):
    """Edita un crédito existente por ID"""
    credito = Credito.query.get_or_404(id)

    if request.method == 'POST':
        try:
            fecha_str = request.form['fecha_otorgamiento']
            fecha = datetime.strptime(fecha_str, "%Y-%m-%d").date()

            credito.cliente = request.form['cliente']
            credito.monto = float(request.form['monto'])
            credito.tasa_interes = float(request.form['tasa_interes'])
            credito.plazo = int(request.form['plazo'])
            credito.fecha_otorgamiento = fecha

            db.session.commit()
            flash('Crédito actualizado exitosamente.', 'success')
            return redirect(url_for('creditos'))

        except Exception as e:
            db.session.rollback()
            flash(f"Error al editar crédito: {str(e)}", 'danger')
            # Opcional: podrías volver a renderizar con los datos actuales y mensaje
            return render_template('editarCredito.html', credito=credito)

    return render_template('editarCredito.html', credito=credito)


# ─────────────────────────────────────────────────────────────
# EJECUCIÓN DE LA APP
# ─────────────────────────────────────────────────────────────


# Punto de entrada
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
    
# ─────────────────────────────────────────────────────────────
# FIN DEL CÓDIGO   