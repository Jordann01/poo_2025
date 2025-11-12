from conexion import Conexion

class Inventario(Conexion):
    def __init__(self, nombre, tipo, cantidad, precio_costo):
        super().__init__()
        self.nombre = nombre
        self.tipo = tipo
        self.cantidad = cantidad
        self.precio_costo = precio_costo

    def guardar(self):
        try:
            sql = "INSERT INTO inventario (nombre, tipo, cantidad, precio_costo) VALUES (:1, :2, :3, :4)"
            datos = (self.nombre, self.tipo, self.cantidad, self.precio_costo)
            self.cursor.execute(sql, datos)
            self.con.commit()
            print("✅ Inventario guardado correctamente.")
        except Exception as e:
            print("❌ Error al guardar inventario:", e)
