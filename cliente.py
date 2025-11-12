from conexion import Conexion

class Cliente(Conexion):
    def __init__(self, nombre, telefono, nacionalidad, habitacion):
        super().__init__()
        self.nombre = nombre
        self.telefono = telefono
        self.nacionalidad = nacionalidad
        self.habitacion = habitacion

    def guardar(self):
        try:
            sql = "INSERT INTO cliente (nombre, telefono, nacionalidad, habitacion) VALUES (:1, :2, :3, :4)"
            datos = (self.nombre, self.telefono, self.nacionalidad, self.habitacion)
            self.cursor.execute(sql, datos)
            self.con.commit()
            print("Cliente guardado correctamente.")
        except Exception as e:
            print(" Error al guardar cliente:", e)
