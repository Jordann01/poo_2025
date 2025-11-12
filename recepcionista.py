from conexion import Conexion

class Usuario:
    def __init__(self, nombre, telefono, ubicacion):
        self.nombre = nombre
        self.telefono = telefono
        self.ubicacion = ubicacion

class Recepcionista(Usuario, Conexion):
    def __init__(self, nombre, telefono, ubicacion):

        
        Usuario.__init__(self, nombre, telefono, ubicacion)
        Conexion.__init__(self)


    def guardar(self):
        try:
            sql = "INSERT INTO usuario (nombre, telefono, ubicacion) VALUES (:1, :2, :3)"
            datos = (self.nombre, self.telefono, self.ubicacion)

            self.cursor.execute(sql, datos)
            self.con.commit()
            print(" Recepcionista guardado correctamente.")
        except Exception as e:

            print("Error al guardar recepcionista:", e)
