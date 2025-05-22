# models.py
from db import db

# Modelos de la base de datos 
class Inventario(db.Model):
    __tablename__ = 'inventario'
    __table_args__ = {'extend_existing': True}
    
    Código_Prod = db.Column(db.Integer, primary_key=True)
    Id_Proveedor = db.Column(db.Integer, db.ForeignKey('proveedores.Id_Proveedor'))
    Nombre_Prod = db.Column(db.Text)
    Precio = db.Column(db.Numeric(10, 2))
    Modelo = db.Column(db.Text)
    Cantidad = db.Column(db.Integer)
    Materiales = db.Column(db.Text)

    proveedor = db.relationship('Proveedores', backref='productos')



class Proveedores(db.Model):
    __tablename__ = 'proveedores'
    __table_args__ = {'extend_existing': True}  # Para evitar errores con nombres de columnas

    
    Id_Proveedor = db.Column(db.Integer, primary_key=True)
    Código_Prod = db.Column(db.Integer)
    Nombre_Prov = db.Column(db.Text)
    Correo = db.Column(db.Text)
    Dirección = db.Column(db.Text)  # Asegúrate de que este campo esté definido correctamente
    Teléfono = db.Column(db.Text)


class Ventas(db.Model):
    Id_venta = db.Column(db.Integer, primary_key=True)
    Id_Paciente = db.Column(db.Integer)
    graduacion_ojo_derecho = db.Column(db.String(100))  # <- asegúrate que esto esté
    graduacion_ojo_izquierdo = db.Column(db.String(100))  # <- y esto también
    Armason = db.Column(db.Text)
    Tratamiento = db.Column(db.Text)
    Anticipo = db.Column(db.Numeric(10,2))
    Adeudo = db.Column(db.Numeric(10,2))
    Fecha = db.Column(db.Date)


class Remesa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Proveedor = db.Column(db.Text)
    CodigoElemento = db.Column(db.Text)
    Modelo = db.Column(db.Text)
    Nombre = db.Column(db.Text)
    Num_Entradas = db.Column(db.Integer)
    Factura = db.Column(db.Text)
    Fecha = db.Column(db.Date)


class Paciente(db.Model):
    Id_Paciente = db.Column(db.Integer, primary_key=True)
    Nombre_Pa = db.Column(db.Text)
    Apellidos = db.Column(db.Text)
    Teléfono1 = db.Column(db.Text)
    Teléfono2 = db.Column(db.Text)
    Dirección = db.Column(db.Integer)
    Correo = db.Column(db.Text)


class Pagos(db.Model):
    Id_Pago = db.Column(db.Integer, primary_key=True)
    Id_Paciente = db.Column(db.Integer)
    Id_Venta = db.Column(db.Integer)
    SaldoAPagar = db.Column(db.Numeric(10,2))
    Abono = db.Column(db.Numeric(10,2))
    SaldoActual = db.Column(db.Numeric(10,2))
    Fecha = db.Column(db.Date)

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    Id_Usuario = db.Column(db.Integer, primary_key=True)
    Nombre = db.Column(db.Text)
    Contraseña = db.Column(db.Text)


