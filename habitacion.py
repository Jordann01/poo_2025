from conexion import Conexion

class Habitacion(Conexion):
    def __init__(self, numero, cantidad_personas, estado):
        super().__init__()
        self.numero = numero
        self.cantidad_personas = cantidad_personas
        self.estado = estado

    def guardar(self):
        try:
            sql = "INSERT INTO habitacion (numero, cantidad_personas, estado) VALUES (:1, :2, :3)"
            datos = (self.numero, self.cantidad_personas, self.estado)
            self.cursor.execute(sql, datos)
            self.con.commit()
            print("Habitación guardada correctamente.")
        except Exception as e:
            print("Error al guardar habitación:", e)
