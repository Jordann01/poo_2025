from conexion import conectar

class Usuario:

    
    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono


class Recepcionista(Usuario):
    def __init__(self, nombre, telefono, ubicacion):

        super().__init__(nombre, telefono)
        self.ubicacion = ubicacion

    def guardar(self):
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute(f"INSERT INTO recepcionista (nombre, telefono, ubicacion) VALUES ('{self.nombre}', '{self.telefono}', '{self.ubicacion}')")
        conexion.commit()
        conexion.close()
        print("Recepcionista guardado")


class Inventario:
    def __init__(self, nombre, tipo, cantidad, precio_costo):
        self.nombre = nombre
        self.tipo = tipo
        self.cantidad = cantidad
        self.precio_costo = precio_costo

    def guardar(self):
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute(f"INSERT INTO inventario (nombre, tipo, cantidad, precio_costo) VALUES ('{self.nombre}', '{self.tipo}', {self.cantidad}, {self.precio_costo})")
        conexion.commit()
        conexion.close()
        print("Producto agregado")


class Habitacion:
    def __init__(self, numero, cantidad_personas, estado):
        self.numero = numero
        self.cantidad_personas = cantidad_personas
        self.estado = estado

    def guardar(self):
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute(f"INSERT INTO habitacion (numero, cantidad_personas, estado) VALUES ({self.numero}, {self.cantidad_personas}, '{self.estado}')")
        conexion.commit()
        conexion.close()
        print("Habitacion guardada")

class Cliente:
    def __init__(self, nombre, telefono, nacionalidad, habitacion):
        self.nombre = nombre
        self.telefono = telefono
        self.nacionalidad = nacionalidad
        self.habitacion = habitacion

    def guardar(self):
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute(f"INSERT INTO cliente (nombre, telefono, nacionalidad, habitacion) VALUES ('{self.nombre}', '{self.telefono}', '{self.nacionalidad}', '{self.habitacion}')")
        conexion.commit()
        conexion.close()
        print("Cliente guardado")





class Boleta:
    def __init__(self, folio, cliente, usuario):
        self.folio = folio
        self.cliente = cliente
        self.usuario = usuario

    def guardar(self):
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute(f"INSERT INTO boleta (folio, cliente, usuario) VALUES ({self.folio}, '{self.cliente}', '{self.usuario}')")
        conexion.commit()
        conexion.close()
        print("Boleta guardada")
